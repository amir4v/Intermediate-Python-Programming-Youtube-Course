# Decorator: function decorator and class decorator

class CountCall:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCall
def hi():
    print("Hi")

hi()
# This is executed 1 times
# Hi

hi()
# This is executed 2 times
# Hi

hi()
# This is executed 3 times
# Hi
