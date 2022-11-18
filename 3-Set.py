# Set: unordered, mutable, no duplicate(managed by itself)

my = {} # it is a dict, you have to use set() method
type(my) # dict
myset = {1,2,3,4,5,1,2}
myset = set([1,2,3,4,5,1,2,3])
myset = set("Hello") # {'H', 'e', 'l', 'o'}
print(myset)

myset.add(2)
myset.remove('l')
myset.discard(4) # just like .remove method but WITHOUT KeyError(if item was not exists)
print(myset)

# myset.clear()

print(myset.pop()) # unordered (like randomly)

for i in myset:
    print(i)

if 2 in myset:
    print("yes")

odds = {1,3,5,7}
evens = {0,2,4,6}
primes = {2,3,5,7}

u = odds.union(evens) # U/+
print(u)

i = odds.intersection(primes) # n
print(i)

diff = odds.difference(primes) # - / A-B / odds-primes
print(diff)

sdiff = odds.symmetric_difference(primes) # (A-B)U(B-A) / (A-B)+(B-A)
print(sdiff)

# odds.update(evens) # In-place
# print(odds)

# odds.intersection_update(primes) # In-place, A = A n B
# print(odds)

# odds.difference_update(primes) # In-place, A = A-B
# print(odds)

# odds.symmetric_difference_update(primes) # In-place, A = (A-B)U(B-A) / A = (A-B)+(B-A)
# print(odds)

print(odds.issubset(primes)) # A is-subset(child)-of B
print(odds.issuperset(primes)) # A is-superset(parent)-of B
print(odds.isdisjoint(evens)) # A n B = {} / Are They Completely Different?

myset = {1,2,3}
copy_set = myset.copy()
copy_set = set(myset)

# Frozen Set (it takes an iterable)
# Build an immutable unordered collection of unique elements.
fset = frozenset([1,2,3])
# fset.add(4) # Error
# fset.remove(1) # Error
