import random

n = int(input("Input number: "))

# может быть precondition loop

while n > 0:
    print(random.random())
    n -= 1

# может быть postcondition loop