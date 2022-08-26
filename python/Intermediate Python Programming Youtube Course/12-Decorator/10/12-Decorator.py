# Decorator: function decorator and class decorator

class CountCall:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(init, *args, **kwargs):
        print("By this, you can call this class instante variable as a method/function")

cc = CountCall(None)
cc()
# it prints 'By this, you can call this class instante variable as a method/function'
