class AppSettings(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings

        return getattr(settings, self.prefix + name, dflt)

    @property
    def ADMIN_LOG_READONLY(self):
        """Prevent log entries from being modified from Django admin."""
        return self._setting("ADMIN_LOG_READONLY", False)

    @property
    def DECODE_REQUEST_BODY(self):
        """
        Allow the request.body byte string to be decoded to a string.

        If you are allowing large file uploads, setting this to False prevents
        a RequestDataTooBig exception.
        """
        return self._setting("DECODE_REQUEST_BODY", True)

    @property
    def PATH_LENGTH(self):
        """Maximum length of request path to log"""
        return self._setting("PATH_LENGTH", 200)


app_settings = AppSettings("DRF_TRACKING_")
