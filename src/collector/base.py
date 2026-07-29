from abc import ABC, abstractmethod

from src.news.models.news import News


class BaseCollector(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def collect(self) -> list[News]:
        ...