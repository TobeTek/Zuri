""" Decorators """
from functools import wraps


def decorator(func):
    # Do something with that func 
    @wraps(func)
    def wrapper(*args, **kwargs):
        no = args[0]
        if not isinstance(no, int) and not isinstance(no, float):
            raise ValueError

        print(f"{func.__name__} was invoked with {args=} and {kwargs=}")
        return func(*args, **kwargs)
    return wrapper 

@decorator
def sqr(no):
    return no ** 2

ans = sqr(5)
sqr("45")

