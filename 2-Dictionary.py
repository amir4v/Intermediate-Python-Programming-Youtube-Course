# Dictionary: Key-Value pairs, unordered, mutable

# Key must be immutable like: Tuple, Int, Str

mydict = {"name": "Amir", "age": "36"}
mydict2 = dict(name="Amir", age=36)

value = mydict["name"]
value = mydict.get("name")
# value = mydict["notexists"] # Error: KeyError
print(mydict.get("notexists")) # returns None
print(mydict.get("notexists", 99)) # returns default value

mydict["name"] = "Reza"
mydict["email"] = "rez@geem.co"

# del mydict["email"]
mydict.pop("email")
mydict.popitem() # removes last item

if "key" in mydict:
    print(mydict["key"])

# for key in mydict:
# for key in mydict.keys():
# for value in mydict.values():
for key, value in mydict.items():
    print(key, value)

dict_copy = mydict.copy()
dict_copy = dict(mydict)

dict1 = {"name": "Amir", "email": "zz@zozo.co"}
dict2 = dict(age=29, name="Reza")
dict1.update(dict2) # update/merge
