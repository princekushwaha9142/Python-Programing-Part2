# A dictionary stores data as key-value pairs. 
# Each key is unique and is used to access the corresponding value. 
# Dictionaries are mutable, meaning you can change their contents after they have been created.

student = {
    "name": "Prince",
    "age": 20,
    "course": "Python"
}

print(student["name"])
print(student["age"])

# Modifying Dictionary 
# Change value

student["age"] = 21

# Add new key
student["marks"] = 95

# Remove key
student.pop("age")

# OR
del student["age"]

# keys()
print(student.keys())

# values()
print(student.values())

# items() 
print(student.items())