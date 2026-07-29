from abc import ABC, abstractmethod

from src.news.models.news import News


class NewsSource(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def fetch(self) -> list[News]:
        ...