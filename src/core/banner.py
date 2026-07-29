from config.app_config import AppConfig


def banner():

    print("=" * 60)
    print(f"{AppConfig.APP_NAME} v{AppConfig.VERSION}")
    print("=" * 60)