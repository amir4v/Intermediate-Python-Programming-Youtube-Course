# List: ordered, mutable, indexed, dynamic, allows duplicate elements

my_list = ["hi", "amir", 1, True, 3.441]
print(my_list)

# my_list2 = list("hi", "amir", 1, True, 3.441) # Error(Wrong)
my_list2 = list({1, 2, 3})
print(my_list2)

item = my_list[0]
item = my_list[-1]
# item = my_list[4] # Error(IndexError) - Index out of range

for i in my_list:
    print(i)

if "hi" in my_list:
    print("yes")
else:
    print("no")

print(len(my_list))

my_list.append("lemon")
print(my_list)

my_list.insert(0, "blueberry")
print(my_list)

item = my_list.pop()
print(item)
print(my_list)

# my_list.remove("Amir1") # Error(ValueError) - Item not found
my_list.remove("amir")
print(my_list)


# my_list.clear()
# print(my_list)

my_list.reverse() # In place
print(my_list)

my_list = [1,3,4,6,2,3,9,45,5,2,1]
my_list.sort() # In place
my_list.sort(reverse=True) # In place
print(my_list)

new_list = sorted(my_list)
print(new_list)

my_list = [0] * 5 # [0, 0, 0, 0, 0]
print(my_list)

my_list2 = [1,2,3,4,5]
new_list = my_list + my_list2
print(new_list)

my_list[1:3] # [start:stop:step] # The last index is excluded

list_org = [1,2,3,4,5]
list_copy = list_org # Both are referring to the same list in RAM
#                    # in First time if you change org/copy then it will change copy/org (ONLY FOR THE FIRST TIME)
# list_org.append(9)
# print(list_copy)
# list_copy.append(9)
# print(list_org)

# For the actual copy
list_copy = list_org.copy()
list_copy = list(list_org)
list_copy = list_org[:]

comprehension_list = [i*i for i in range(5)]
print(comprehension_list)
