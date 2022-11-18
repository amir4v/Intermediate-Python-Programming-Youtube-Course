# Generators: (like yield): returns an object (single object) at the moment that you can iterate over it; it returns it lazyly that mean one object at the time; and Generators are soo memory efficient

def my_generator():
    yield 1
    yield 2

g = my_generator()
print(g) # <generator object my_generator at 0x7fc294d6ab20>
for i in g:
    print(i) # 1 2

g = my_generator()
v = next(g)
print(v) # 1
v = next(g)
print(v) # 2
# v = next(g) # Error: StopIteration
# print(v)

g = my_generator()
print(sum(g)) # 3

g = my_generator()
print(sorted(g, reverse=True)) # [2, 1]

def countdown(num):
    print("Satrting")
    while num > 0:
        yield num
        num -= 1
cd = countdown(2)
print(next(cd))
# Satrting
# 2
print(next(cd))
# 1

# Efficiency
import sys
def firstn(n):
    nums = []
    num = 0
    while num <= n:
        nums.append(num)
        num += 1
    return nums
def firstn_generator(n):
    num = 0
    while num <= 0:
        yield num
        num += 1
print(sys.getsizeof(firstn(1000))) #8856
print(sys.getsizeof(firstn_generator(1000))) # 104

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b
fib = fibonacci(11)
for f in fib:
    print(f)

rng  = range(10)
print(rng) # range(0, 10)

# Generator Expression
mygenerator = (i for i in range(10))
print(mygenerator) # <generator object <genexpr> at 0x7f8c9b416c70>
print(list(mygenerator)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mylist = [i for i in range(10)]
print(mylist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mygenerator = (i for i in range(1000))
mylist = [i for i in range(1000)]
print(sys.getsizeof(mygenerator), '-', sys.getsizeof(mylist)) # 104 - 8856
