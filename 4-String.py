# String: ordered, immutable, indexed

mystring = "hello"
mystring = 'hello i\'m amir'
print(mystring)

mystring = '''hello
i'm amir'''
mystring = """hello
i'm amir"""
print(mystring)

# \ says: don't go next line, This continues and The next line is the continuation of this line
mystring = """hello \
world"""
print(mystring)

mystring = "hello"
char = mystring[0]

# mystring[0] = 'h' # (Error) TypeError: 'str' object does not support item assignment

first = "Hi"
second = "John"
greeting = first + " " + second

for i in greeting:
    print(i)

if 'J' in greeting:
    print("Yes")
else:
    print("No")

mystring = '   Gi    '
print(mystring.strip()) # 'Gi'
mystring = '---------hi--'
print(mystring.strip('-')) # 'hi'

mystring = 'hTTp'
print(mystring.upper()) # HTTP
print(mystring.lower()) # http
print(mystring.title()) # Http
print(mystring.startswith("hT")) # True
print(mystring.endswith("Tp")) # True
print(mystring.find("Tp")) # index of first, >>> 2
print(mystring.count("T")) # 2
print(mystring.replace("Tp", "ml")) # hTml

mystring = "Hi-how-are-you?"
mylist = mystring.split("-") # ['Hi', 'how', 'are', 'you?'] # default: .split()/" "/.split(" ")
print(mylist)
print(" ".join(mylist)) # Hi how are you?

from timeit import default_timer
start = default_timer()
for i in range(5):
    i**i**i
stop = default_timer()
print(stop-start)

# Formatting: %, .format(), f-String
svar = "VAR"
ivar = 123
fvar = 1.23
print("the string formatting %s" %svar)
print("the string formatting %d" %ivar)
print("the string formatting %.2f" %fvar)
print("the string formatting {} {} {:.2f}".format(svar, ivar, fvar))
print(f"the string formatting {svar} {ivar*2} {fvar}")
