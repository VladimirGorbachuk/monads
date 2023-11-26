from typing import Any, Callable, Coroutine, Optional


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
    
    def bind(self, func: Callable) -> "MonadWithException":
        if self._exception:
            return self
        try:
            value = func(self.value)
            return MonadWithException(value=value)
        except Exception as e:
            self._exception = e
            return self


class AsyncMonadWithException:
    def __init__(
            self,
            *,
            value: Any,
            coroutine: Optional[Coroutine] = None,
            exception: Optional[Exception] = None,
        ) -> None:
        self._value = value
        self._coroutine = coroutine
    
    async def get_value(self) -> Any:
        return await self._coroutine
    
    def async_bind(self, func: Coroutine) -> "AsyncMonadWithException":
        if not self._coroutine:
            self._coroutine = func(self._value)
            return self
        async def new_coroutine():
            res = await self._coroutine
            return await func(res)
        self._coroutine = new_coroutine
        return self
