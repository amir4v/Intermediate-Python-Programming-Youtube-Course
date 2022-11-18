# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

mystring = "aaabbc"
c = Counter(mystring) # Counter({'a': 3, 'b': 2, 'c': 1}) # it's a dict .items()/.keys()/.values() .get("KEY") ["KEY"]
print(c.most_common(2)) # [('a', 3), ('b', 2)]

c.elements() # gives us a iterable
print(list(c.elements())) # ['a', 'a', 'a', 'b', 'b', 'c']

Point = namedtuple('Point', 'x,y')
p = Point(2,5)
print(type(p)) # <class '__main__.Point'>
print(p) # Point(x=2, y=5)
print(p.x, p.y) # 2 5

# Now from Python-3.7 , OrderedDict and dict are same and dict remembers order
od = OrderedDict() # == {key: value} == dict
od["a"] = 1
od["b"] = 2
print(od) # OrderedDict([('a', 1), ('b', 2)])

# defaultdict is just like dict and OrderedDict but it has a default value if the key has not been set yet
d = defaultdict(int) # int/str/float/bool/list/tuple/set/dict/... # if dont give it an argument like defaultdict() , it'll be same as a normal dict
d['a'] = 1
d['b'] = 2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['c']) # >>> 0

# deque: double ended queue that means you can add/remove element from both ends
d = deque()
d.append(1)
d.append(2)
print(d) # deque([1, 2])
d.appendleft(3)
print(d) # deque([3, 1, 2])
print(d.pop()) # >>> 2
print(d) # deque([3, 1])
print(d.popleft()) # >>> 3
print(d) # deque([1])
# d.clear()
d.extend([2,3,4])
print(d) # deque([1, 2, 3, 4])
d.extendleft([5,6,7])
print(d) # deque([7, 6, 5, 1, 2, 3, 4])
d.rotate(2) # default is 1 , also yo can use negative numbers like -1
print(d) # deque([3, 4, 7, 6, 5, 1, 2])
