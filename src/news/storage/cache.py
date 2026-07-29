import json
from pathlib import Path

from src.news.models.news import News


class NewsCache:

    FILE = Path("src/news/storage/news_cache.json")

    def save(self, news: list[News]):

        data = []

        for item in news:

            data.append(
                {
                    "title": item.title,
                    "url": item.url,
                    "source": item.source,
                    "summary": item.summary,
                    "image": item.image,
                    "language": item.language,
                    "category": item.category,
                    "score": item.score,
                    "country": item.country,
                    "tags": item.tags
                }
            )

        with open(self.FILE, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )