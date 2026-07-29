from src.collector.manager import CollectorManager

from src.news.sources.steam import SteamSource
from src.news.sources.rockstar import RockstarSource
from src.news.sources.ign import IGNSource


class CollectorRegistry:

    @staticmethod
    def build():

        manager = CollectorManager()

        manager.register(SteamSource())
        manager.register(RockstarSource())
        manager.register(IGNSource())

        return manager