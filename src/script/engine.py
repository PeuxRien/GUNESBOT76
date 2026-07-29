from src.script.models import Script


class ScriptEngine:

    def generate(self, news):

        return Script(

            title=news.title,

            duration=45,

            text=f"""
Did you hear this?

{news.title}

This is currently one of the hottest gaming stories.

Stay tuned for more.
"""

        )