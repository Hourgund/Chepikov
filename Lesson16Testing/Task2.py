def factorial(number):
    f = 1

    for item in range(2, number + 1):
        f *= item

    return f


def main():
    f = int(input("Input your number: "))
    msg = factorial(f)
    print(msg)


main()
