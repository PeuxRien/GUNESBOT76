import requests


class Request:

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    @staticmethod
    def get(url: str):

        response = requests.get(
            url,
            headers=Request.HEADERS,
            timeout=20
        )

        response.raise_for_status()

        return response.text