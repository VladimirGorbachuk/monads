from tcr import MonadWithException, Omg, wtf
from example_funcs import factorial

import pytest


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
    monad.bind(lambda x: x)