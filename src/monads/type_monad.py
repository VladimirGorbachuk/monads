from typing import Callable, Generic, TypeVar


ValueType = TypeVar("ValueType")
ReturnedValueType = TypeVar("ReturnedValueType")


class MonadType(Generic[ValueType]):
    _value: ValueType

    def bind(self, func: Callable[[ValueType], ReturnedValueType]) -> "MonadType[ReturnedValueType]":
        raise NotImplementedError
