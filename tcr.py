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
            value: Optional[Any] = None,
            coroutine: Optional[Coroutine] = None,
            exception: Optional[Exception] = None,
        ) -> None:
        self._value = value
        self._coroutine = coroutine
        self._exception = exception
    
    async def get_value(self) -> Any:
        if self._exception:
            raise self._exception
        if self._coroutine:
            return await self._coroutine
        return self._value
    
    def async_bind(self, func: Coroutine) -> "AsyncMonadWithException":
        async def new_coroutine():
            value = await self.get_value()
            try:
                new_value = await func(value)
                return AsyncMonadWithException(value=None, coroutine=self._coroutine, exception=self._exception)
            except Exception as e:
                return AsyncMonadWithException(value=self._value, coroutine=self._coroutine, exception = e)
        return AsyncMonadWithException(value=self._value, exception=self._exception, coroutine=new_coroutine)
