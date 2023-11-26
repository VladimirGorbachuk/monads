from tcr import AsyncMonadWithException, MonadWithException, Omg, wtf
from example_funcs import factorial

import pytest
import pytest_asyncio


def test_wtf():
    assert 1==1


def test_wtf_2():
    assert wtf(2, 3) == 5


def test_wtf_3():
    assert wtf("a", "b") == "ab"


def test():
    assert "" == ""


def test_omg():
    omg = Omg()
    assert omg + omg == omg
    assert omg + 1 == omg
    assert omg - 1 == omg


def test_ooo():
    assert 1==1
    assert 2==2
    assert 3==3


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



async def _add_one(value):
    return value + 1


@pytest.mark.asyncio
async def test_async_monad_get_value():
    async_monad = AsyncMonadWithException(value=1)
    assert await async_monad.get_value() == 1