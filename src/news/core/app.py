from src.core.banner import banner
from src.core.logger.logger import Logger

from src.news.core.engine import NewsEngine


class OdinApp:

    def run(self):

        banner()

        Logger.info("Loading News Engine")

        engine = NewsEngine()

        news = engine.load()

        print()

        print("=" * 60)

        print(f"Toplam Haber: {len(news)}")

        print()

        for item in news[:10]:

            print("-", item["title"])

        print()

        Logger.info("Done.")