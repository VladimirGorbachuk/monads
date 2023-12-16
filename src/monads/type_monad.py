from typing import Generic, TypeVar


ValueType = TypeVar("ValueType")


class MonadType(Generic[ValueType]):
    _value: ValueType
