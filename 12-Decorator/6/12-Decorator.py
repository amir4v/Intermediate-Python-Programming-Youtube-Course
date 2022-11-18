# Decorator: function decorator and class decorator

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start") # Start
        result = func(*args, **kwargs)
        print("End")   # End
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

print(help(add5))
"""
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
~
~
~
~
~
(END)
"""

print(add5.__name__)
# wrapper
