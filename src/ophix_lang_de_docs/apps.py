from django.apps import AppConfig


class OphixLangDeDocsConfig(AppConfig):
    name = "ophix_lang_de_docs"
    verbose_name = "Ophix German — Documentation"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(_import_docs, sender=self)


def _import_docs(sender, **kwargs):
    try:
        from django.core.management import call_command
        call_command(
            "ophix_docs_update",
            include_app_docs="ophix_lang_de_docs",
            language="de",
            verbosity=0,
        )
    except Exception:
        pass
