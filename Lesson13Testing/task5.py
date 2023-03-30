while True:
    number = int(input("Input positive number: "))

    if number > 0:
        break
    else:
        print("Invalid data! Number should be positive!\nTry again...")

print(number)
