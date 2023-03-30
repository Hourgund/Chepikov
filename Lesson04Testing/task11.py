# 1) result value
# 2) type: unary, binary, ternary
# 3) group:
# 4) priority
# 5)
# a = 10
# a = a * 2
# a = a + 100 # a += 100
# fdgfdg = 10
# fdgfdg = fdgfdg + 10
# fdgfdg += 10

a = 10
b = 20

print ("Before: a = ", a, "; b = ", b)

# 1
# t = a
# a = t
# b = t

# 2
# a = a + b  # 30
# b = a - b  # 10
# a = a - b  # 20

# 3
# a = a * b  # 200
# b = a / b  # 10
# a = a / b  # 20

# 4
# a, b = b, a



print ("After swaping: a = ", a, "; b = ", b)