class PromptBuilder:

    def build(self, news):

        return f"""
You are a professional YouTube Shorts script writer.

Language: English

Duration: 45 seconds

Topic:

{news.title}

Write:

Hook

Story

Ending

Only return narration.
"""