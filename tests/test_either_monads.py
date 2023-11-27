from monads.either_monads import EitherMonad, EitherMonadEnum


def test_instantiates_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.RIGHT)
    assert either_instance.is_right is True


def test_instantiates_not_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.LEFT)
    assert either_instance.is_right is False


def test_righ_binds_right_func():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.RIGHT)
    new_instance = either_instance.bind_either_funcs(lambda x: x-1, lambda x: x+1)
    assert new_instance.is_right is True
    assert new_instance.value == 4


def test_left_binds_left_func():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.LEFT)
    new_instance = either_instance.bind_either_funcs(lambda x: x-1, lambda x: x+1)
    assert new_instance.is_right is False
    assert new_instance.value == 2


# the tests above are not true either (funcs should return either monad, not just process values)
