import feedparser

from src.collector.base import BaseCollector
from src.news.models.news import News


RSS_URL = "https://feeds.ign.com/ign/games-all"


class IGNSource(BaseCollector):

    @property
    def name(self) -> str:
        return "IGN"

    def collect(self) -> list[News]:

        feed = feedparser.parse(RSS_URL)

        news = []

        for item in feed.entries:

            news.append(
                News(
                    title=item.title,
                    url=item.link,
                    source="IGN"
                )
            )

        return news