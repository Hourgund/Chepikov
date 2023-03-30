def math(n, m):
    if n == 0 or m == 0:
        return "Wrong data!"

    return n % m == 0


def main():
    n = int(input("Input your number: "))
    m = int(input("Is it multiple to "))
    msg = "Yes" if math(n, m) else "No"
    print(msg)


main()
