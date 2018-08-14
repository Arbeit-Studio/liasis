from liasis.core.config import AppConfig


def config_of(application: Text) -> AppConfig:
    try:
        from config import APPS
        app_config = APPS.get(application, None)
        if not app_config:
            import apps
            app_module = getattr(apps, application)
            app_config = app_module.config.DefaultConfig
        return app_config
    except:
        raise
        