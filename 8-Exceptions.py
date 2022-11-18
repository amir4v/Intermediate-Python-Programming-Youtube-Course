# Exceptions: Errors and Exceptions

# a = 5 print(a) # SyntaxError: invalid syntax

# a = 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# import somemodule # ModuleNotFoundError: No module named 'somemodule'

# a = c # NameError: name 'c' is not defined

# f = open('somefile.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

a = [1,2]
# a.remove(3) # ValueError: list.remove(x): x not in list

# a[2] # IndexError: list index out of range

d = {"name": "Max"}
# d["age"] # KeyError: 'age'

# raise
x = -3
# if x < 0:
#     raise Exception("x should be positive") # Exception: x should be positive

# assert
# assert x>=0, "x is not positive" # AssertionError: x is not positive

try:
    a = 5 / 0
except:
    print("an errot happend")

try:
    a = 5 / 0
except Exception as e:
    print(e) # division by zero

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

try:
    a = 5 / 0
    b = 5 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

try:
    a = 5
except Exception as e:
    print(e)
finally:
    print("finally block will run however and it's not important your code has an Exception or not")

try:
    a = 5
except Exception as e:
    print(e)
else:
    print("if you have not an Exception and your code is fine this else block will run")

try:
    a = 4
except Exception as e:
    print(e)
else:
    print("code is fine")
finally:
    print("finally / cleaning operations")

# Custom Exception
class ValueToHighError(Exception):
    pass # This is valid

a = 30
# if a > 10:
#     raise ValueToHighError("Error message for to high value error") # __main__.ValueToHighError: Error message for to high value error

try:
    if a > 10:
        raise ValueToHighError("Error message for to high value error") # __main__.ValueToHighError: Error message for to high value error
except ValueToHighError as e:
    print(e) # Error message for to high value error

try:
    if a > 10:
        raise ValueToHighError("Error message for to high value error") # __main__.ValueToHighError: Error message for to high value error
except Exception as e:
    print(e) # Error message for to high value error

a = 1
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
try:
    if a < 5:
        raise ValueTooSmallError("value is too small", a)
except ValueTooSmallError as e: # except Exception as e:
    print(e.message, e.value) # value is too small 1
