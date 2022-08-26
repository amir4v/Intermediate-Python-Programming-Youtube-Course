# Decorator: function decorator and class decorator

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

result = add5(11) # None
print(result) # None
"""
Start
End
None
"""
