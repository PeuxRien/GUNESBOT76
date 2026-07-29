import feedparser

from src.collector.base import BaseCollector
from src.news.models.news import News


RSS_URL = "https://store.steampowered.com/feeds/news.xml"


class SteamSource(BaseCollector):

    @property
    def name(self):

        return "Steam"

    def collect(self):

        feed = feedparser.parse(RSS_URL)

        news = []

        for item in feed.entries:

            news.append(
                News(
                    title=item.title,
                    url=item.link,
                    source="Steam"
                )
            )

        return news