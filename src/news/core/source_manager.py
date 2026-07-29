from src.news.core.source import NewsSource
from src.core.logger.logger import Logger


class SourceManager:

    def __init__(self):
        self.sources = []

    def register(self, source: NewsSource):
        self.sources.append(source)

    def fetch_all(self):

        news = []

        Logger.info(f"{len(self.sources)} source registered.")

        for source in self.sources:

            Logger.info(f"Checking {source.name}...")

            try:

                result = source.fetch()

                if not result:
                    Logger.warning(f"{source.name}: No news returned.")
                else:
                    Logger.success(f"{source.name}: {len(result)} news")

                news.extend(result)

            except Exception as e:

                Logger.error(f"{source.name}: {str(e)}")

        return news