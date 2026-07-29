from src.media.models import MediaAsset


class MediaFinder:

    def search(self, scene):

        return [

            MediaAsset(

                title=scene.description,

                source="Internet",

                path="",

                score=0,

                media_type="video",

                duration=scene.duration

            )

        ]