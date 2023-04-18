students = {"Alex": 10, "Peter": 9, "Victor": 7,
            "Anna": 8, "Kate": 8, "Vladimir": 10,
            "Nikita": 8}

print(students["Anna"])  # 8
print(students.get("Anna"))  # 8
# print(students["Alice"]) Key error
print(students.get("Alice"))  # None
print(students.get("Alice", 0))  # 0
