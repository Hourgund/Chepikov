def call_age(age):
    if not (0 <= age <= 150):
        return "Wrong Data"

    if age <= 13:
        msg = "Childhood"
    elif age <= 34:
        msg = "Youth"
    elif age <= 59:
        msg = "Maturity"
    else:
        msg = "Old age"

    # else:
    # msg = "Wrong Data"

    return msg


def main():
    age = int(input("Input your age: "))
    print(call_age(age))


main()
