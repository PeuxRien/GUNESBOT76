from src.ai.models import VideoDecision
from src.ai.classifier import CategoryClassifier


class DecisionEngine:

    def __init__(self):

        self.classifier = CategoryClassifier()

    def analyze(self, news):

        category = self.classifier.classify(
            news.title
        )

        create = news.score >= 20

        reason = (
            "High Trend Score"
            if create
            else
            "Low Trend Score"
        )

        priority = int(news.score)

        return VideoDecision(

            title=news.title,

            score=news.score,

            should_create=create,

            reason=reason,

            category=category,

            priority=priority

        )