a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))
d = int(input("Input D: "))

# max min arithmetic_avg geometrical_avg
# business logic

if a > b and a > c and a > d:
    max = a
elif b > c and b > d:
    max = b
elif c > d:
    max = c
else:
    max = d

msg = ' Max value is {} '.format(max)
print(msg)

avg = (a * b * c * d) ** (1 / 4)
msg1 = " Avg value is {} ".format(avg)
print(msg1)
