# birth 3
# 0 100 + 3
# 101 200 +2
# 201 +1
age = int(input("Input age: "))

if age <= 0:
    msg = "User Data was invalid!"
else:

    head = 3

    if age <= 100:
        head += age * 3
    elif age <= 200:
        head += 300 + (age - 100) * 2
    else:
        head += 500 + (age - 200) * 1

    msg = "Dragon had {} heads".format(head)
print(msg)
