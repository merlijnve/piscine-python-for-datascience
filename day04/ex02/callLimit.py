from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call too many times")
                return
        return limit_function
    return callLimiter
