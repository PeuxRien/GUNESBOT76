from rapidfuzz import fuzz


class Deduplicator:

    def clean(self, news):

        result = []

        titles = []

        for item in news:

            duplicate = False

            for title in titles:

                if fuzz.ratio(item.title.lower(), title.lower()) > 92:
                    duplicate = True
                    break

            if not duplicate:
                titles.append(item.title)
                result.append(item)

        return result