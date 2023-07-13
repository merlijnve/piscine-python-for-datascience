def square(x: int | float) -> int | float:
    """Square the input."""
    return x * x


def pow(x: int | float) -> int | float:
    """Raise 2 to the power of the input."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return the inner count function."""
    count = x

    def inner() -> float:
        nonlocal count
        try:
            count = function(count)
            return count
        except Exception as e:
            print(e)
            return 0
    return inner
