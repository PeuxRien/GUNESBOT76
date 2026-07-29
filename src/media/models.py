from dataclasses import dataclass


@dataclass
class MediaAsset:

    title: str

    source: str

    path: str

    score: float

    media_type: str

    duration: float