class TrendScorer:

    KEYWORDS = {

        "gta": 30,
        "gta 6": 50,
        "rockstar": 20,
        "ea sports": 15,
        "battlefield": 20,
        "call of duty": 15,
        "fortnite": 10,
        "minecraft": 10,
        "playstation": 10,
        "xbox": 10,
        "steam": 5
    }

    def calculate(self, news):

        title = news.title.lower()

        score = 0

        for keyword, value in self.KEYWORDS.items():

            if keyword in title:

                score += value

        news.score = score

        return news