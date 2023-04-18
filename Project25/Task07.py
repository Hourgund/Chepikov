students = {"Alex": 10, "Peter": 9, "Victor": 7,
            "Anna": 8, "Kate": 8, "Vladimir": 10,
            "Nikita": 8}

# print(len(students))

# print(students.keys())
#for element in students.keys():
#    print(element)

# print(students.values())
#for element in students.values():
#    print(element)

# for key in students.keys():
#    print(key + " - " + str(students[key]))

# for item in students.items():
#    print(item)

for key, value in students.items():
    print(key, " - ", value)

# key, value = item