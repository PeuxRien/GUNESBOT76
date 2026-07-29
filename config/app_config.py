from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    APP_NAME = "ODIN AI"
    VERSION = "0.0.2"

    DEFAULT_LANGUAGE = "de"

    DEFAULT_VIDEO_DURATION = 45

    DEBUG = True

    AUTHOR = "Arda"