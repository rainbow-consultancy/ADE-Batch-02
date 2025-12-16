# 1. list -- mutable datatype
# 2. tuple -- immutable datatype
# 3. set
# 4. dict


# list

# fruits1 = ['apple', 'mango', 'kiwi']
# fruits2 = ["pineapple", "Grapes"]

# fruits = fruits1 + fruits2
# print(fruits)

# fruits1.extend(fruits2)
# print(fruits1)

# fruits1.append(fruits2)
# print(fruits1)

# print(fruits)

# # add a new fruit to the list
# fruits.append('banana')
# print(fruits)

# # print(fruits[-1])

# # syntax --> [start:stop:step]
# # print(fruits[-1:-3:-1])

# print(fruits.index("banana"))

# print(fruits.count("apple"))

# print(len(fruits))


# fruits.pop()
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# tuple
# fruits = ('apple', 'mango', 'kiwi')
# print(fruits)
# print(type(fruits))

# fruits.append("Grape")

# print(fruits[1])


# set

fruits = {'apple', 'mango', 'kiwi', 'mango'}
print(fruits)

fruits.add("Orange")
# print(fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)
# print(set3)

common_set = set1.intersection(set2)
# print(common_set)

diff_set = set1.difference(set2)
# print(diff_set)


# dict

student = {
    "name": "Dileep",
    "age": 24,
    "course": "Python"
}

print(student["name"])

student["age"] = 25
print(student)

student["city"] = "Bangalore"
print(student)

print(student.get("name"))

