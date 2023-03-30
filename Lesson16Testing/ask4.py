def check_all_even_digits(number):
    while number > 0:
        digit = number % 10
        if digit % 2 == 1:
            return False
        number //= 10

    return True

def main():
    number = int(input("Input your number: "))
    msg = check_all_even_digits(number)
    print(msg)


main()

