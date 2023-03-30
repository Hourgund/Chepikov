from random import randrange

SIDE_COUNT = 2


def throw_coin(count):
    heads = 0
    counter = 0

    if count <= 0:
        return 0, 0

    while counter < count:
        side = randrange(SIDE_COUNT)

        if side == 0:
            heads += 1

            counter += 1

    return heads, count - heads


def main():
    count = int(input("Input number of roles: "))
    heads, tails = throw_coin(count)

    msg = "Number of heads is {}, number of tails: {}.".format(heads, tails)
    print(msg)


main()
