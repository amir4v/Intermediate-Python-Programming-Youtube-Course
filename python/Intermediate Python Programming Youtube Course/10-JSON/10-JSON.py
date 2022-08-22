# JSON: JavaScript Object Notation

import json

person = {"name": "Amir", "age": 6, "titles":["Scientist", "Developer"]}
personJSON = json.dumps(person)
print(personJSON) # {"name": "Amir", "age": 6, "titles": ["Scientist", "Developer"]}

personJSON = json.dumps(person, indent=True)
print(personJSON)
'''
{
 "name": "Amir",
 "age": 6,
 "titles": [
  "Scientist",
  "Developer"
 ]
}
'''

personJSON = json.dumps(person, indent=4)
print(personJSON)
'''
{
    "name": "Amir",
    "age": 6,
    "titles": [
        "Scientist",
        "Developer"
    ]
}
'''

personJSON = json.dumps(person, indent=4, separators=('; ', '= '))
print(personJSON)
'''
{
    "name"= "Amir"; 
    "age"= 6; 
    "titles"= [
        "Scientist"; 
        "Developer"
    ]
}
'''

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
'''
{
    "age": 6,
    "name": "Amir",
    "titles": [
        "Scientist",
        "Developer"
    ]
}
'''

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

personJSON = """
{
    "name": "Amir",
    "age": 23,
    "areyou": true,
    "titles": [
        1,
        2,
        3
    ]
}
"""
person = json.loads(personJSON)
print(person) # {'name': 'Amir', 'age': 23, 'areyou': True, 'titles': [1, 2, 3]}

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person) # {'name': 'Amir', 'age': 6, 'titles': ['Scientist', 'Developer']}

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
u = User("Amir", 22)
# userJSON = json.dumps(u) # TypeError: Object of type User is not JSON serializable
def encode_user(o):
    if isinstance(o, User):
        return {"name":o.name, "age":o.age, o.__class__.__name__:True}
    else:
        raise TypeError("The o object is not JSON Serializable")
userJSON = json.dumps(u, default=encode_user)
print(userJSON) # {"name": "Amir", "age": 22, "User": true}

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name":o.name, "age":o.age, o.__class__.__name__:True}
        else:
            raise TypeError("The o object is not JSON Serializable")
u = User("Amir", 22)
userJSON = json.dumps(u, cls=UserEncoder)
print(userJSON) # {"name": "Amir", "age": 22, "User": true}
#
userJSON = UserEncoder().encode(u)
print(userJSON) # {"name": "Amir", "age": 22, "User": true}

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    else:
        return dct
user = json.loads(userJSON, object_hook=decode_user)
print(type(user)) # <class '__main__.User'>
