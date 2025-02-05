from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    verbose_name = "Servisler"
    
    def ready(self):
        import service.signals