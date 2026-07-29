from src.media.finder import MediaFinder
from src.media.ranker import MediaRanker


class MediaEngine:

    def __init__(self):

        self.finder = MediaFinder()

        self.ranker = MediaRanker()

    def search(self, scenes):

        assets = []

        for scene in scenes:

            assets.extend(

                self.finder.search(scene)

            )

        return self.ranker.rank(assets)