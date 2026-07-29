class MediaRanker:

    def rank(self, assets):

        return sorted(

            assets,

            key=lambda x: x.score,

            reverse=True

        )