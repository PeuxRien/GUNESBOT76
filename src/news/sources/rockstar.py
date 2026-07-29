from urllib.parse import urljoin

from src.collector.base import BaseCollector
from src.news.models.news import News

from src.crawler.request import Request
from src.crawler.parser import Parser


URL = "https://www.rockstargames.com/newswire"


class RockstarSource(BaseCollector):

    @property
    def name(self):

        return "Rockstar"

    def collect(self):

        html = Request.get(URL)

        soup = Parser.html(html)

        news = []

        articles = soup.find_all("a")

        for article in articles:

            href = article.get("href")

            if not href:
                continue

            if "/newswire/article/" not in href:
                continue

            title = article.get_text(" ", strip=True)

            if len(title) < 10:
                continue

            news.append(
                News(
                    title=title,
                    url=urljoin(URL, href),
                    source="Rockstar"
                )
            )

        return news