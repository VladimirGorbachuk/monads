from typing import Any, Awaitable, Callable, Coroutine, List, Optional


class MonadWithException:
    def __init__(self, *, value: Any, exception: Optional[Exception] = None) -> None:
        self._value = value
        self._exception = exception

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MonadWithException):
            return self._value == other._value and self._exception == other._exception
        return False

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


class LazyEvalMonadWithException:
    def __init__(
            self,
            *,
            value: Any,
            exception: Optional[Exception] = None,
            bind_stack: Optional[List[Callable]] = None,
        ) -> None:
        self._value = value
        self._exception = exception
        print("current bind stack", bind_stack)
        if bind_stack is None:
            self._bind_stack = []
        else:
            self._bind_stack = bind_stack

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LazyEvalMonadWithException):
            return self._value == other._value and self._exception == other._exception
        return False
    
    @property
    def value(self) -> Any:
        if self._exception:
            raise self._exception
        for func in self._bind_stack:
            self = self._bind_and_calculate(func)
            if self._exception:
                raise self._exception
        return self._value
    
    def bind(self, func: Callable) -> "LazyEvalMonadWithException":
        return LazyEvalMonadWithException(
            value=self._value, 
            exception=self._exception,
            bind_stack=self._bind_stack+[func],
        )

    def _bind_and_calculate(self, func: Callable) -> "LazyEvalMonadWithException":
        if self._exception:
            return self
        try:
            print("called?")
            value = func(self._value)
            return LazyEvalMonadWithException(value=value)
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
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, AsyncMonadWithException):
            return self._value == other._value and self._coroutine == other._coroutine and self._exception == other._exception
        return False

    async def get_value(self) -> Any:
        if self._exception:
            raise self._exception
        if self._coroutine:
            monad = await self._coroutine
            return await monad.get_value()
        return self._value
    
    def async_bind(self, func: Callable[[Any], Awaitable]) -> "AsyncMonadWithException":
        async def new_coroutine() -> AsyncMonadWithException:
            value = await self.get_value()
            try:
                new_value = await func(value)
                return AsyncMonadWithException(value=new_value, exception=self._exception)
            except Exception as e:
                return AsyncMonadWithException(value=self._value, exception = e)
        return AsyncMonadWithException(value=self._value, exception=self._exception, coroutine=new_coroutine())
    
    def bind(self, func: Callable) -> "AsyncMonadWithException":
        async def func_as_coroutine(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return self.async_bind(func_as_coroutine)
