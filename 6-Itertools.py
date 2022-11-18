# Itertools: prodect, permutations, combinations, accumulate, groupby

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

# product
a = [1, 2]
b = [3]
p = list(product(a, b))
print(p) # [(1, 3), (2, 3)]
p = list(product(a, b, repeat=2))
print(p) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

# permutations/جایگشت: all possible ordering
a = [1, 2, 3]
perm = list(permutations(a))
print(perm) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = list(permutations(a, 2)) # 2 means: Two together (dota dota ba ham)
print(perm) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations/ترکیبات: 
a = [1, 2, 3, 4]
comb = list(combinations(a, 2))
print(comb) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] # without replacement
comb_w_r = list(combinations_with_replacement(a, 2))
print(comb_w_r) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)] # khodesh ba khodesh

# accumulate/انباشتن
a = [1, 2, 3, 4]
acc = list(accumulate(a))
print(acc) # [1, 3, 6, 10]

import operator
acc = list(accumulate(a, func=operator.mul))
print(acc) # [1, 2, 6, 24]

a = [1, 2, 5, 3, 4]
#   [1, 2, 5, 5, 5]
acc = list(accumulate(a, max)) # min
print(acc) # [1, 2, 5, 5, 5]

print(max([1,2,3,4])) # >>> 4
print(min(1,2,3,4)) # >>> 1

# groupby
def smaller_than_3(x):
    return x<3
a = [1,2,3,4]
g = groupby(a, key=smaller_than_3)
for key, value in g:
    print(key, list(value))
    # True  [1, 2]
    # False [3, 4]

a = [1,2,3,4]
g = groupby(a, key=lambda x: x<3)
for key, value in g:
    print(key, list(value))

persons = [
    {"name": "Amir", "age": 25},
    {"name": "Abed", "age": 25},
    {"name": "Reza", "age": 27},
]
g = groupby(persons, key=lambda x: x["age"])
for key, value in g:
    print(key, list(value))
# 25 [{'name': 'Amir', 'age': 25}, {'name': 'Abed', 'age': 25}]
# 27 [{'name': 'Reza', 'age': 27}]

# count(start): starts from start for infinite
# for i in count(10):
#     print(i) # 10 11 12 13 ...

# cycle: it goes through an iterable for infinite
# a = [1, 2, 3]
# for i in cycle(a):
#     print(i) # 1 2 3 1 2 3 1 2 3 1 2 3 ...

for x in repeat(2, 4): # repeat(object, HowMenyTimes)
    print(x) # 2 2 2 2
