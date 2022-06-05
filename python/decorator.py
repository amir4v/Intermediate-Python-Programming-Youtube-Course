import functools


def my_decorator(x, y): # Decorator-e Kamel Ba Vorodi(x, y)
    def decorator(func): # Decorator-e Bedone Vorodi
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(x ** y)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@my_decorator(3, 5)
def my_function():
    print("my_function")


my_function()
