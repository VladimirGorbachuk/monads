def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("cannot get factorial of a negative integer")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result