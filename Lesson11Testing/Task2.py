import random

random.seed(1)

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))
print(round(random.random() * 100, 2))
print(random.random() * 100)

random.seed(2)

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))
print(round(random.random() * 100, 2))
print(random.random() * 100)
