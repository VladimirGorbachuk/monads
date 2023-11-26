from typing import Any, Callable, Optional, Union


def wtf(first, second):
    return first + second


class Omg():
    def __add__(self, other):
        return self
    
    def __sub__(self, other):
        return self
    

class MonadWithException:
    def __init__(self, *, value: Any, exception: Optional[Exception] = None) -> None:
        self._value = value
        self._exception = exception
    
    @property
    def value(self) -> Any:
        if self._exception:
            raise self._exception
        return self._value
         