number = int(input("Input your number: "))

# DRY !!!!

# number = 12345

s = number % 10     # a = 5

number //= 10       # 1234
s += number % 10    # b = 4

number //= 10       # 123
s += number % 10    # c = 3

number //= 10       # 12
s += number % 10    # d = 2

s += number // 10   # e = 1

print("Sum of number digits is", s)