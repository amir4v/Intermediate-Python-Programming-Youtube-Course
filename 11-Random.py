# Random

import random

r = random.random()
print(r) # a float number between 0 and 1 : 0.6188272815630717

r = random.uniform(1, 10)
print(r) # a float number between 1 and 10 : 3.243880442289352

r = random.randint(1, 10) # a int number between 1 and 10 (both included) : 9
print(r)

r = random.randrange(1, 10) # a int number between 1and 9 (10 excluded) : 8
print(r)

# for statistic
r = random.normalvariate(mu=0, sigma=3)
print(r)

mylist = list("ASDFGHJKL") # ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
print(random.choice(mylist)) # picks a random single element: 'L'
print(random.choices(mylist)) # picks a random single element and give it as a list: ['L']
print(random.choices(mylist, k=3)) # picks 3 random (not unique) element
print(random.sample(mylist, 3)) # picks 3 random unique element

print(mylist) # ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
random.shuffle(mylist) # shuffles the list in-place
print(mylist) # ['S', 'L', 'K', 'F', 'G', 'A', 'H', 'D', 'J']

# seed: reproduce that random number with that specific seed value
random.seed(1)
print(random.randint(1, 100)) # 18
random.seed(1)
print(random.randint(1, 100)) # 18

# secrets: it's just like random but more random but it takes more time
import secrets
s = secrets.randbelow(100) # (int) and 100 is not included
print(s)

s = secrets.randbits(8) # yek adade 8 bit-e random tolid mikone
print(s) # 195

print(secrets.choice(mylist)) # single random element

# numpy
import numpy as np
a = np.random.rand(3, 3) # 3x3 array (3 rows and 3 columns) and each cell is filled by a random float number 0-1
print(a)

a = np.random.randint(1, 100, 3) # an array with 3 integer-random elements
print(a) # [6 68 99]

a = np.random.randint(1,100, (3,3)) # an 3x3 array that filled with integer-random elements
print(a)
np.random.shuffle(a) # it's just shuffles surface indices - in-place

a = np.array([[1,2], [3,4], [5,6]]) # makes an array from specified values

# numpy seed
np.random.seed(1)
a = np.random.rand(3)
print(a) # [4.17022005e-01 7.20324493e-01 1.14374817e-04]
np.random.seed(1)
a = np.random.rand(3)
print(a) # [4.17022005e-01 7.20324493e-01 1.14374817e-04]
