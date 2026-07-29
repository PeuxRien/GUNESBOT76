from src.news.core.source_manager import SourceManager

from src.news.sources.steam import SteamSource
from src.news.sources.rockstar import RockstarSource
from src.news.sources.ign import IGNSource


class SourceRegistry:

    @staticmethod
    def build() -> SourceManager:

        manager = SourceManager()

        manager.register(SteamSource())
        manager.register(RockstarSource())
        manager.register(IGNSource())

        return manager