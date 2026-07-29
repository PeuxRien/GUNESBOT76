from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class News:

    title: str

    url: str

    source: str

    published: datetime | None = None

    summary: str = ""

    image: str = ""

    language: str = "en"

    category: str = "gaming"

    country: str = "global"

    tags: list[str] = field(default_factory=list)

    score: float = 0.0

    def __str__(self):

        return (
            f"[{self.source}] "
            f"{self.title} "
            f"(Score: {self.score:.1f})"
        )