# Tuple: ordered, immutable, indexed, allows duplicate elements

mytuple = 1,
mytuple = (1,)

mytuple = (1, 2.222, True, "Hi")
mytuple = 1, 2.222, True, "Hi"
print(mytuple)

mytuple = tuple([1,2,3,2,3,5,5,5,5])

# mytuple[0] = "value" # TypeError: 'tuple' object does not support item assignment

print(mytuple.count(5))

print(mytuple.index(5)) # (The first one) index of 5 value
# mytuple.index('notinthetuple') # ValueError: tuple.index(x): x not in tuple

info_tuple = ("Amir", 23, "Tehran")
name, age, city = info_tuple # UnPacking
print(name, age, city)

mytuple = (1,2,3,4,5,)
first_item, *middle_items, last_item = mytuple
print(first_item, middle_items, last_item) # 1 [2, 3, 4] 5

import sys
my_tuple = (i**i for i in range(1000))
my_list = [i**i for i in range(1000)]
print(sys.getsizeof(my_tuple)) # (gets in bytes) 112
print(sys.getsizeof(my_list)) # [gets in bytes] 9016

import timeit
# stmt = Statement (whatever python script)
print( timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=10000) ) # 7.090000053722179e-05
print( timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=10000) ) # 0.000672399999530171
