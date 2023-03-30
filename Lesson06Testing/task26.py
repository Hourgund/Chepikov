number = int(input("Input your number: "))
number = number if number >= 0 else -number  # number *= 1 if nuber >= 0 else -1
msg = "Absolute value is " + str(number)
print(msg)
