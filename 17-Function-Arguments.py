# Function-Arguments

"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args , **kwargs)
- Container unpacking into function arguments
- Local vs. gloabl arguments
- Parameter passing (by value , by reference)
"""

# def add5(number): # number is a Parameter
# add(6) # 6 is a Argument

# def foo(a, b, c):
# foo(1, 2, 3) # Positional arguments
# foo(a=2, b=2, c=3) # Keyword arguments
# foo(1, b=2, c=3)
# foo(1, b=2, 3) # Error: Can not use positional argument after keyword argument
# foo(1, b=2, a=3) # Error: Got multiple values for argument 'a'

# def foo(a, b=2): # Default argument
# def foo(a, b=2, c): # Error: Can not put non-default argument after a default argument

# def foo(a, b, *args, **kwargs): # args is a tuple, kwargs is a dict/dictionary
# foo(1,2, 3,4, five=5, six=6)
# foo(1,2)
# foo(1,2, seven=7)

# def foo(a,b, *, c,d): # required keyword-only arguments: all after asteriks arguments are keyword arguments by force
    # print(a,b,c,d)
# foo(1,2,3,4) # TypeError: foo() takes 2 positional arguments but 4 were given
# foo(1,2) # TypeError: foo() missing 2 required keyword-only arguments: 'c' and 'd'
# foo(1,2, c=3, d=4)

# def foo(*, a, b): # all arguments are: required keyword-only arguments
    # print(a,b)
# foo(1,2) # TypeError: foo() takes 0 positional arguments but 2 were given
# foo(a=1) # TypeError: foo() missing 1 required keyword-only argument: 'b'
# foo(a=1,b=2)

# def foo(*args, last):
#     for arg in args:
#         print(arg)
#     print(last)
# foo(1,2,3) # TypeError: foo() missing 1 required keyword-only argument: 'last'
# foo(1, last=2)
# foo(last=3)

# def foo(**kwargs):
#     print(kwargs)
# foo(1) # TypeError: foo() takes 0 positional arguments but 1 was given
# foo(a=1) # {'a': 1}

# def foo(**kwargs, a): # SyntaxError: invalid syntax

# def foo(a, **kwargs):

# def foo(a,b,c):
#     print(a,b,c)
# mylist = [1,2,3] # or tuple
# foo(*mylist) # the number of parameters must be the same as number of arguments # >>> 1 2 3
# mydict = {'a':1, 'b':2, 'c':3}
# foo(**mydict) # the number-and-names of parameters must be the same as number-and-names of arguments # >>> 1 2 3

# def foo():
#     x = number
#     # x is a local variable
#     print(x)
# number = 3 # global
# foo() # 3

# number = 3 # global
# def foo():
#     x = number
#     # x is a local variable
#     print(x)
# foo() # 3

# def foo():
#     x = number
#     number = 4 # (Error): UnboundLocalError: local variable 'number' referenced before assignment
#     # x is a local variable
#     print(x)
# number = 3 # global
# foo()

# def foo():
#     x = number
#     global number
#     number = 4
#     # x is a local variable
#     print(x)
# number = 3 # global
# foo()
# (Error): SyntaxError: name 'number' is used prior to global declaration

# def foo():
#     global number # using global variable in a function
#     x = number
#     number = 4
#     # x is a local variable
#     print(x)
# number = 3 # global
# foo() # 3
# print(number) # 4

# def foo():
#     number = 2 # local-variable
# number = 3 # global-variable
# print(number) # will print the global varable: 3

# Call-by-Value , Call-by-Reference
# in Python: Call-by-Object , Call-by-Object-Reference
# Immutable and Mutable

# def foo(x):
#     x = 5
# y = 10
# foo(y)
# print(y) # 10

# def foo(xlist):
#     xlist[0] = 5
# ylist = [10, 3]
# foo(ylist)
# print(ylist) # [5, 3]

# def foo(alist):
#     alist = [200, 300, 400]
# blist = [1, 2, 3]
# foo(blist)
# print(blist) # [1, 2, 3]

# def foo(a_list):
#     a_list += [5]
# b_list = [1, 2]
# foo(b_list)
# print(b_list) # [1, 2, 5]

# def foo(a_list):
#     a_list = a_list + [5]
# b_list = [1, 2]
# foo(b_list)
# print(b_list) # [1, 2]
