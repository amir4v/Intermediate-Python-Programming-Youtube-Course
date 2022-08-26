# Decorator: function decorator and class decorator

import functools

def start_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # repr(obj) # نمایش رشته متعارف شی را برگردانید == {key!r} == variable!r >>> on jori namayesh mide ke dar cod nevisi neveshte shode: masalan 'str' mizare on jaee ke neveshti: strvar!r
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k!r}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr+kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug #     First
@start_end # Second
def say_hi(name):
    print(f"Hi {name}")
    return f"Hi {name}"

say_hi(name="Amir")
"""
Calling say_hi('name'='Amir')
START
Hi Amir
END
'say_hi' returned 'Hi Amir'
"""

# Tozihate Mohem
"""
aval @debug ejra mishe
va vaghti dakhele @debug, func ejra mishe: result = func(*args, **kwargs)
on vaght in ejra mishe:
[
    @start_end
    def say_hi(name):
        print(f"Hi {name}")
        return f"Hi {name}"
]
badesh edame @debug ejra mishe yani:
[
    print(f"{func.__name__!r} returned {result!r}")
    return result
]
"""
