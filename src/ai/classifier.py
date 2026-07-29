class CategoryClassifier:

    KEYWORDS = {

        "GTA": [
            "gta",
            "rockstar",
            "gta online",
            "gta 6"
        ],

        "Call of Duty": [
            "call of duty",
            "black ops",
            "warzone"
        ],

        "Fortnite": [
            "fortnite"
        ],

        "PlayStation": [
            "playstation",
            "ps5",
            "sony"
        ],

        "Xbox": [
            "xbox"
        ],

        "Nintendo": [
            "nintendo",
            "switch"
        ],

        "Steam": [
            "steam"
        ]
    }

    def classify(self, title: str):

        title = title.lower()

        for category, words in self.KEYWORDS.items():

            for word in words:

                if word.lower() in title:

                    return category

        return "General Gaming"