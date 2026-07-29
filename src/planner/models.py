from dataclasses import dataclass


@dataclass
class Scene:

    order: int

    description: str

    duration: float