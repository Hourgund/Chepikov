def count_coin(amount):
    count = amount // 50
    amount %= 50

    count += amount // 25
    amount %= 25

    count += amount // 10
    amount %= 10

    count += amount // 5
    amount %= 5

    count += amount

    return count


def main():
    amount = int(input("Input amount of money: "))

    count = count_coin(amount)

    msg = "You should pay {} coins".format(count)

    print(msg)


main()
