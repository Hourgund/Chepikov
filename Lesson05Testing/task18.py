# 12345 --> 54321
# input block
number = int(input("Input your number: "))

# a = number % 10
# b = number % 100 // 10
# c = number % 1000 // 100
# d = number % 10000 // 1000
# e = number // 10000
# s = str(a)+ str(b) + str(c) + str(d) + str(e)

# business logic block
number_copy = number

reverse_number = number % 10  # reverse_number = 5
number //= 10  # number = 1234
reverse_number *= 10  # reverse_number = 50

reverse_number += number % 10  # reverse_number = 54
number //= 10  # number = 123
reverse_number *= 10  # reverse_number = 540

reverse_number += number % 10  # reverse_number = 543
number //= 10  # number = 12
reverse_number *= 10  # reverse_number = 5430

reverse_number += number % 10  # reverse_number = 5432
reverse_number *= 10  # reverse_number = 54320
reverse_number += number // 10  # reverse_number = 54321

# output block
print("Your number: ", number_copy)
print("Reversed number is: ", reverse_number)