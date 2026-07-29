from src.trend.keywords import HOT_KEYWORDS


class TrendScore:

    @staticmethod
    def calculate(title: str):

        score = 0

        title = title.lower()

        for keyword, value in HOT_KEYWORDS.items():

            if keyword in title:
                score += value

        return score