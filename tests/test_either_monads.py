from monads.either_monads import EitherMonad, EitherMonadEnum


def test_instantiates_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.RIGHT)
    assert either_instance.is_right is True


def test_instantiates_not_is_right():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.LEFT)
    assert either_instance.is_right is False


def test_right_binds_right_func():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.RIGHT)
    new_instance = either_instance.bind_either_funcs(lambda x: x-1, lambda x: x+1)
    assert new_instance.is_right is True
    assert new_instance.value == 4


def test_left_binds_left_func():
    either_instance = EitherMonad(value=3, either_enum=EitherMonadEnum.LEFT)
    new_instance = either_instance.bind_either_funcs(lambda x: x-1, lambda x: x+1)
    assert new_instance.is_right is False
    assert new_instance.value == 2


def _either_binding_callable_zero_division(monad: EitherMonad) -> EitherMonad:
    if monad.is_right:
        try:
            return EitherMonad(value=1/monad.value, either_enum=EitherMonadEnum.RIGHT)
        except ZeroDivisionError as e:
            return EitherMonad(value=e, either_enum=EitherMonadEnum.LEFT)
    else:
        return monad


def test_zero_division_either_monadic_callable_for_right() -> EitherMonad:
    monad = EitherMonad(value=1, either_enum=EitherMonadEnum.RIGHT)
    assert monad.bind(_either_binding_callable_zero_division).is_right is True


def test_zero_division_either_monadic_callable_for_right_with_exception_gives_left() -> EitherMonad:
    monad = EitherMonad(value=0, either_enum=EitherMonadEnum.RIGHT)
    assert monad.bind(_either_binding_callable_zero_division).is_right is False


def test_zero_division_either_monadic_callable_for_left() -> EitherMonad:
    monad = EitherMonad(value=ValueError("all gone wrong"), either_enum=EitherMonadEnum.LEFT)
    res_monad = monad.bind(_either_binding_callable_zero_division)
    assert res_monad.is_right is False
    assert isinstance(res_monad.value, ValueError) is True


def test_zero_division_either_monadic_callable_pipe_error_follows_with_left_func() -> EitherMonad:
    monad = EitherMonad(value=0, either_enum=EitherMonadEnum.RIGHT)
    zde_monad = monad.bind(_either_binding_callable_zero_division)
    bool_valued_monad = zde_monad.bind_either_funcs(lambda x: isinstance(x, ZeroDivisionError), lambda x: x+1)
    assert bool_valued_monad.value is True
