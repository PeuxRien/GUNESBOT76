from src.core.logger.logger import Logger

from src.collector.registry import CollectorRegistry

from src.news.services.normalizer import Normalizer
from src.news.services.deduplicator import Deduplicator
from src.news.storage.cache import NewsCache
from src.news.analyzer.trend_score import TrendScorer

from src.ai.decision import DecisionEngine


class NewsEngine:

    def __init__(self):

        self.collector = CollectorRegistry.build()

        self.normalizer = Normalizer()

        self.deduplicator = Deduplicator()

        self.scorer = TrendScorer()

        self.cache = NewsCache()

        self.decision = DecisionEngine()

    def load(self):

        Logger.info("Collecting News...")

        news = self.collector.collect()

        Logger.info("Normalizing...")

        news = self.normalizer.normalize(news)

        Logger.info("Removing duplicates...")

        news = self.deduplicator.clean(news)

        Logger.info("Scoring...")

        scored = []

        for item in news:

            scored.append(
                self.scorer.calculate(item)
            )

        scored.sort(
            key=lambda x: x.score,
            reverse=True
        )

        Logger.info("Saving cache...")

        self.cache.save(scored)

        Logger.success(
            f"{len(scored)} unique news collected."
        )

        Logger.info("AI Decision Engine...")

        decisions = []

        for item in scored:

            decisions.append(
                self.decision.analyze(item)
            )

        Logger.success(
            f"{len(decisions)} video decisions created."
        )

        print("\n============================================================")
        print("VIDEO DECISIONS")
        print("============================================================\n")

        for d in decisions:

            status = "YES" if d.should_create else "NO"

            print(
                f"[{status}] "
                f"{d.category:<15} "
                f"Score:{d.score:<5} "
                f"{d.title}"
            )

        return scored