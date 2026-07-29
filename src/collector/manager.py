from src.core.logger.logger import Logger
from src.collector.base import BaseCollector


class CollectorManager:

    def __init__(self):

        self.collectors: list[BaseCollector] = []

    def register(self, collector: BaseCollector):

        self.collectors.append(collector)

    def collect(self):

        Logger.info(f"{len(self.collectors)} collectors loaded.")

        news = []

        for collector in self.collectors:

            Logger.info(f"Running {collector.name}...")

            try:

                result = collector.collect()

                Logger.success(
                    f"{collector.name}: {len(result)}"
                )

                news.extend(result)

            except Exception as e:

                Logger.error(
                    f"{collector.name}: {e}"
                )

        return news