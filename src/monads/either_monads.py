from enum import Enum
from typing import Any, Callable


class EitherMonadEnum(Enum):
    LEFT = "left"
    RIGHT = "right"


class EitherMonad:
    def __init__(self, value: Any, either_enum: EitherMonadEnum):
        self.value = value
        self.is_right = either_enum is EitherMonadEnum.RIGHT

    def bind_either_funcs(self, left_func: Callable, right_func: Callable) -> "EitherMonad":
        if self.is_right:
            return self.__class__(value=right_func(self.value), either_enum=EitherMonadEnum.RIGHT)
        return self.__class__(value=left_func(self.value), either_enum=EitherMonadEnum.LEFT)

    def bind(self, either_func: Callable[["EitherMonad"], "EitherMonad"]) -> "EitherMonad":
        return either_func(self)
