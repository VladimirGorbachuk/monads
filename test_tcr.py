from tcr import Omg, wtf

import pytest


def test_wtf():
    assert 1==1


def test_wtf_2():
    assert wtf(2, 3) == 5


def test_wtf_3():
    assert wtf("a", "b") == "ab"


def test():
    assert "" == ""