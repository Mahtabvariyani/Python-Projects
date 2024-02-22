""" Dictionaries """

# they are used to story a Collection Data
# they are changeable but not Dublicated


students = [
    {
        "name": "John",
        "age": 20,
        "major": "Computer Science",
        "GPA": 3.5
    },
    {
        "name": "Emily",
        "age": 21,
        "major": "Engineering",
        "GPA": 3.8
    },
    {
        "name": "Michael",
        "age": 19,
        "major": "Mathematics",
        "GPA": 3.2
    },
]


for student in students:
    for key, value in student.items():
        print(key, "=", value)

""" 
if "name" in student:
    print("it does exists", student["name"])
else:
    print("it doesnt exist")


try:
    print(student["age"])
except KeyError:
    print("The value Does not Exists")
 """

""" 
the diffrence between if else and try exept is that the if else is comparing but try and exept is just handling the answer 

"""

# print(student["name"])
# print(type(student))


# student2=dict(name="Mah",language="Farsi")
# print(student2)
# print(type(student2))
