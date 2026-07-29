class KeywordExtractor:

    def extract(self, title: str):

        title = title.lower()

        keywords = []

        if "gta" in title:
            keywords.append("GTA 6 Gameplay")

        if "rockstar" in title:
            keywords.append("Rockstar Games Logo")

        if "casino" in title:
            keywords.append("Diamond Casino")

        if "online" in title:
            keywords.append("GTA Online")

        if "fortnite" in title:
            keywords.append("Fortnite Gameplay")

        if "call of duty" in title:
            keywords.append("Call of Duty Gameplay")

        return keywords