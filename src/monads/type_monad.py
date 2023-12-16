from typing import Generic, TypeVar


ValueType = TypeVar("ValueType")
CallableBoundType = TypeVar("CallableBoundType")


class MonadType(Generic[ValueType]):
    _value: ValueType

    def bind(self, func: CallableBoundType) -> "MonadType":
        raise NotImplementedError
