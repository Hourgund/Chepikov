age = int(input("Input age: "))

# 1)
if age <= 0:
    age *= -1
# 2 )
#  age = age if age >= 0 else -age
head = 3

if age <= 100:
    head += age * 3
elif age <= 200:
    head += 300 + (age - 100) * 2
else:
    head += 500 + (age - 200) * 1

msg = "Dragon had {} heads".format(head)
print(msg)
