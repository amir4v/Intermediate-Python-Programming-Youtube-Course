# Decorator: function decorator and class decorator

import functools

def repeat(times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Amir")
"""
Hello Amir
Hello Amir
Hello Amir
"""
