from random import randrange


SIDE_COUNT = 2


def throw_coin(count):
    heads = 0
    tails = 0

    while count > 0:
        side = randrange(SIDE_COUNT)
        if side == 0:
            heads += 1
        else:
            tails += 1

        count -= 1

    return heads, tails


def main():
    count = int(input("Input number of roles: "))
    heads, tails = throw_coin(count)

    msg = "Number of heads is {}, number of tails: {}.".format(heads, tails)
    print(msg)


main()
