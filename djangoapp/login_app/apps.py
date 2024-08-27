from django.apps import AppConfig

class LoginAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_app'
    # add this
    def ready(self):
        import login_app.signals  # noqa

