from bs4 import BeautifulSoup


class Parser:

    @staticmethod
    def html(text: str):

        return BeautifulSoup(
            text,
            "html.parser"
        )