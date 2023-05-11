import datetime

from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.urls import path
from django.http import JsonResponse

from .app_settings import app_settings
from .models import APIRequestLog


class APIRequestLogAdmin(admin.ModelAdmin):
    date_hierarchy = "requested_at"
    list_display = (
        "id",
        "requested_at",
        "response_ms",
        "status_code",
        "user",
        "view_method",
        "path",
        "remote_addr",
        "host",
        "query_params",
    )
    ordering = ("-requested_at",)
    list_filter = ("view_method", "status_code")
    search_fields = (
        "path",
        f"user__{app_settings.LOOKUP_FIELD}",
    )
    raw_id_fields = ("user",)

    if app_settings.ADMIN_LOG_READONLY:
        readonly_fields = (
            "user",
            "username_persistent",
            "requested_at",
            "response_ms",
            "path",
            "view",
            "view_method",
            "remote_addr",
            "host",
            "method",
            "query_params",
            "data",
            "response",
            "errors",
            "status_code",
            "user_agent"
        )

    def changelist_view(self, request, extra_context=None):
        # Aggregate api logs per day
        chart_data = (
            APIRequestLog.objects.annotate(date=TruncDay("requested_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        extra_context = extra_context or {"chart_data": list(chart_data)}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        # convert start_date and end_date to datetime objects
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        chart_data = self.chart_data(start_date, end_date)
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self, start_date, end_date):
        return (
            APIRequestLog.objects.filter(
                requested_at__date__gte=start_date, requested_at__date__lte=end_date
            )
            .annotate(date=TruncDay("requested_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )


admin.site.register(APIRequestLog, APIRequestLogAdmin)
