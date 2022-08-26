# Decorator: function decorator and class decorator

import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start") # Start
        result = func(*args, **kwargs)
        print("End")   # End
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

print(add5.__name__)
# add5
