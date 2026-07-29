from src.news.sources.steam import SteamSource


class SourceManager:

    def fetch_all(self):

        news = []

        steam = SteamSource().fetch()

        print(f"Steam: {len(steam)} haber bulundu.")

        news.extend(steam)

        return news