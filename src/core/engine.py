from src.news.core.source_manager import SourceManager


class NewsEngine:

    def load(self):

        manager = SourceManager()

        return manager.fetch_all()