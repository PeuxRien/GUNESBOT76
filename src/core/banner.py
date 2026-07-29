from config.app_config import APP_NAME, VERSION

def banner():

    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print("=" * 60)