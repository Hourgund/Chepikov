number = int(input("Input your number: "))

# X % 6 = 0 1 2 3 4 5
# 12345 = 15
# 10000 + 2000 + 300 + 40 + 5
# 12345 % 10 --> 5
# 12345 // 10 --> 1234
# 1234 % 10 --> 4

# number = 12345

a = number % 10 # a = 5
b = number % 100 // 10 # b = 4
c = number % 1000 // 100 # c = 3
d = number % 10000 // 1000 # d = 2
e = number // 10000  # e = 1

s = str(a)+ str(b) + str(c) + str(d) + str(e)
print("Sum of number digits is ", s)



