# while first <= last
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 12]
# middle = (first + last) // 2
# 1) search == ls[middle]
# 2) search > ls[middle] --> first = middle + 1
# 3) search < ls[middle] --> last = middle - 1
# return False
def binary_searching(ls, value):
    first = 0
    last = len(ls) - 1

    while first <= last:
        middle = (first + last) // 2
        if value == ls[middle]:
            return True
        elif value > ls[middle]:
            first = middle + 1
        else:
            last = middle - 1

    return False


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_searching(ls, 3))
print(binary_searching(ls, 33))
