# Lambda: lambda arguments: expression

add = lambda x,y: x+y
print(add(4,5)) # >>> 9

p = lambda o: print(o)
p("hi")

a = [(1,4), (-3,6), (2,4), (5,3)]
sa = sorted(a)
print(sa) # [(-3, 6), (1, 4), (2, 4), (5, 3)] # by default sorted method use first argument of tuple

sa2 = sorted(a, key=lambda x: x[1])
print(sa2) # [(5, 3), (1, 4), (2, 4), (-3, 6)] # according to Y index or 1 index

def sort_by_y(x): # 1/Y
    return x[1]
sa2 = sorted(a, key=sort_by_y)
print(sa2) # [(5, 3), (1, 4), (2, 4), (-3, 6)]

a = [(11,4), (5,3), (1,4), (-3,6), (2,4)]
#   [(-3, 6), (1, 4), (2, 4), (5, 3), (11, 4)]
s = sorted(a, key=lambda x: x[0] + x[1])
print(s) # [(-3, 6), (1, 4), (2, 4), (5, 3), (11, 4)]

# map: map(func, sequenceLikeAList)
a = [1,2,3,4,5]
b = list(map(lambda x: x*x, a))
print(b) # [1, 4, 9, 16, 25]

list_comprehension = [x*x for x in a] # comprehension/درک مطلب
print(list_comprehension) # [1, 4, 9, 16, 25]

# filter
a = [1,2,3,4,5,6,7]
b = list(filter(lambda x: x%2==0, a))
print(b) # [2, 4, 6]
c = [x for x in a if x%2==0]
print(c) # [2, 4, 6]

# reduce
from functools import reduce
a = [1,2,3,4]
b = reduce(lambda x,y: x+y, a)
print(b) # (1+2)+3)+4) # >>> 10
