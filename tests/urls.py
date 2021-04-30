# coding=utf-8
from __future__ import absolute_import

import django
from rest_framework.routers import DefaultRouter

from . import views as test_views

if django.VERSION[0] == 1:
    from django.conf.urls import include
else:
    from django.urls import include, re_path

router = DefaultRouter()
router.register(r'user', test_views.MockUserViewSet)

urlpatterns = [
    re_path(r'^no-logging$', test_views.MockNoLoggingView.as_view()),
    re_path(r'^logging$', test_views.MockLoggingView.as_view()),
    re_path(r'^logging-exception$', test_views.MockLoggingView.as_view()),
    re_path(r'^slow-logging$', test_views.MockSlowLoggingView.as_view()),
    re_path(r'^explicit-logging$', test_views.MockExplicitLoggingView.as_view()),
    re_path(r'^sensitive-fields-logging$', test_views.MockSensitiveFieldsLoggingView.as_view()),
    re_path(r'^invalid-cleaned-substitute-logging$', test_views.MockInvalidCleanedSubstituteLoggingView.as_view()),
    re_path(r'^custom-check-logging-deprecated$', test_views.MockCustomCheckLoggingViewDeprecated.as_view()),
    re_path(r'^custom-check-logging$', test_views.MockCustomCheckLoggingView.as_view()),
    re_path(r'^custom-check-logging-methods$', test_views.MockCustomCheckLoggingWithLoggingMethodsView.as_view()),
    re_path(r'^custom-check-logging-methods-fail$', test_views.MockCustomCheckLoggingWithLoggingMethodsFailView.as_view()),
    re_path(r'^custom-log-handler$', test_views.MockCustomLogHandlerView.as_view()),
    re_path(r'^errors-logging$', test_views.MockLoggingErrorsView.as_view()),
    re_path(r'^session-auth-logging$', test_views.MockSessionAuthLoggingView.as_view()),
    re_path(r'^token-auth-logging$', test_views.MockTokenAuthLoggingView.as_view()),
    re_path(r'^json-logging$', test_views.MockJSONLoggingView.as_view()),
    re_path(r'^multipart-logging$', test_views.MockMultipartLoggingView.as_view()),
    re_path(r'^streaming-logging$', test_views.MockStreamingLoggingView.as_view()),
    re_path(r'^validation-error-logging$', test_views.MockValidationErrorLoggingView.as_view()),
    re_path(r'^404-error-logging$', test_views.Mock404ErrorLoggingView.as_view()),
    re_path(r'^500-error-logging$', test_views.Mock500ErrorLoggingView.as_view()),
    re_path(r'^415-error-logging$', test_views.Mock415ErrorLoggingView.as_view()),
    re_path(r'^no-view-log$', test_views.MockNameAPIView.as_view()),
    re_path(r'^view-log$', test_views.MockNameViewSet.as_view({'get': 'list'})),
    re_path(r'^400-body-parse-error-logging$', test_views.Mock400BodyParseErrorLoggingView.as_view()),
    re_path(r'', include(router.urls))
]
