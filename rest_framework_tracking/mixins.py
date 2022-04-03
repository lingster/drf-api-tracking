from .base_mixins import BaseLoggingMixin
from .models import APIRequestLog


class LoggingMixin(BaseLoggingMixin):
    def handle_log(self):
        """
        Hook to define what happens with the log.

        Defaults on saving the data on the db.
        """
        if self.delete_log_days_period is not None:
            from django.utils import timezone
            now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())
            delete_before_date_time = now - datetime.timedelta(days=self.delete_log_days_period)
            APIRequestLog.objects.filter(view=self.log['view'], requested_at__lt=delete_before_date_time).delete()
        APIRequestLog(**self.log).save()


class LoggingErrorsMixin(LoggingMixin):
    """
    Log only errors
    """

    def should_log(self, request, response):
        return response.status_code >= 400
