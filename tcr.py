assert 23==23
assert 4==4
assert 5==5


def wtf(first, second):
    return first + second


class Omg():
    def __add__(self, other):
        return Omg()