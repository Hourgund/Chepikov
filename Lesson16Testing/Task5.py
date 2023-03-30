def some(condition):
    msg = "Error"

    if condition == 10:
        msg = "1"
    elif condition == 20:
        msg = "2"

    return msg


print(some(100))
