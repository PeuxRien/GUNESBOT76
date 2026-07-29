import re

from src.news.models.news import News


class Normalizer:

    def normalize(self, news: list[News]) -> list[News]:

        for item in news:

            title = item.title.lower()

            title = re.sub(r"[^a-z0-9\s]", "", title)

            title = re.sub(r"\s+", " ", title)

            item.title = title.strip()

        return news