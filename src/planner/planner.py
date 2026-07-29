from src.planner.models import Scene
from src.planner.extractor import KeywordExtractor


class ScenePlanner:

    def __init__(self):

        self.extractor = KeywordExtractor()

    def create(self, news):

        scenes = []

        keywords = self.extractor.extract(news.title)

        order = 1

        for keyword in keywords:

            scenes.append(

                Scene(

                    order=order,

                    description=keyword,

                    duration=4.0

                )

            )

            order += 1

        return scenes