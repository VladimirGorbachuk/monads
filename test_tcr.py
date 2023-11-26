from tcr import AsyncMonadWithException, MonadWithException
from example_funcs import async_add_one, factorial, async_divide_one_by_value

import pytest


def test_monad():
    monad = MonadWithException(value=1)
    res = monad.bind(lambda x: x)
    assert res.value == 1


def test_monad_factorial():
    monad = MonadWithException(value=2)
    res = monad.bind(factorial)
    assert res.value == 2


def test_monad_zero_division():
    monad = MonadWithException(value = 0)
    res = monad.bind(lambda x: 1/x)
    with pytest.raises(ZeroDivisionError):
        res.value


def test_monad_pipe():
    monad = MonadWithException(value=1)
    res = monad.bind(lambda x: x+1).bind(lambda x: x+1)
    assert res.value == 3


def test_monad_pipe_keeps_exception():
    monad = MonadWithException(value = 0)
    res = monad.bind(lambda x: 1/x).bind(lambda x: x+1)
    with pytest.raises(ZeroDivisionError):
        res.value


@pytest.mark.asyncio
async def test_async_monad_get_value():
    async_monad = AsyncMonadWithException(value=1)
    assert await async_monad.get_value() == 1


@pytest.mark.asyncio
async def test_async_monad_get_value():
    async_monad = AsyncMonadWithException(value=1)
    assert await async_monad.get_value() == 1


@pytest.mark.asyncio
async def test_async_monad_async_bind():
    async_monad = AsyncMonadWithException(value=1)
    result_monad = async_monad.async_bind(async_add_one)
    assert await result_monad.get_value() == 2


@pytest.mark.asyncio
async def test_async_monad_async_bind_pipe():
    async_monad = AsyncMonadWithException(value=1)
    result_monad = async_monad.async_bind(async_add_one).async_bind(async_add_one)
    assert await result_monad.get_value() == 3


@pytest.mark.asyncio
async def test_async_monad_raises():
    async_monad = AsyncMonadWithException(value=0)
    result_monad = async_monad.async_bind(async_divide_one_by_value).async_bind(async_add_one)
    with pytest.raises(ZeroDivisionError):
        await result_monad.get_value()