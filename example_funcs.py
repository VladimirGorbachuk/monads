def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("cannot get factorial of a negative integer")
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


async def add_one(value):
    return value + 1



async def async_add_one(value):
    return value + 1