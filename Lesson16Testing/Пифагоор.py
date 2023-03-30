def pythagorean_table(size):
    table = ''

    for multy in range(1, size + 1):
        for item in range(1, size + 1):
            table += str(item * multy) + "\t"

        table += "\n"

    return table


print(pythagorean_table(10))