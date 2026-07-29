from dataclasses import dataclass


@dataclass
class VideoDecision:

    title: str

    score: float

    should_create: bool

    reason: str

    category: str

    priority: int