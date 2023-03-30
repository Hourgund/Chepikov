a = int(input("Input your first number: "))
b = int(input("Input your second number: "))

maxvelue = a if a > b else b
minvelue = a if a < b else b

msg = "Max value is " + str(maxvelue)
msg += "\nMin value is " + str(minvelue)

print(msg)