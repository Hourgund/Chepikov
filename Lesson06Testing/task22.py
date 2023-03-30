a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

exist = a + b > c and b + c > a and c + a > b

result = exist and (a == b or a == c or b == c)

msg = "Can this triangle be isosceles?"
msg += "\nAnswer: " + str(result)
print (msg)