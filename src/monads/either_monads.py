from enum import Enum
from typing import Any


class EitherMonadEnum(Enum):
    LEFT = "left"
    RIGHT = "right"


class EitherMonad:
    def __init__(self, value: Any, either_enum: EitherMonadEnum):
        self.value = value
        self.is_right = either_enum is EitherMonadEnum.RIGHT
