from random import randint

a = int(input("Where we start? "))
b = int(input("Where we stop? "))

# active fool-proof
if a > b:
    a, b = b, a

print(randint(a, b))
print(randint(a, b))
print(randint(a, b))
