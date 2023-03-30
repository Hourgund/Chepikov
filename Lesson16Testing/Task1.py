

ls = [45, 67, 89, 345, 6]

index = 0
while index < len(ls):
    print(ls[index], end=' ')
    index += 1

print()

index = len(ls) - 1
while index >= 0:
    print(ls[index], end=' ')
    index -= 1

print()

students = []

for value in ls:
    print(value, end=' ')

print()

for index in range(len(ls)):
    print(ls[index], end=' ')

print()

for index in range(len(ls) - 1, -1, -1):
    print(ls[index], end=' ')