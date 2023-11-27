from monads.either_monads import EitherMonad, EitherMonadEnum


def test_instantiates_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.RIGHT)
    assert either_instance.is_right is True


def test_instantiates_not_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.LEFT)
    assert either_instance.is_right is False
