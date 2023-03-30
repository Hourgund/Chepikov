# simple python script with triangle
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
result = a + b > c and b + c > a and c + a > b
msg = "Can this triangle exist?"
msg += "\nAnswer: " + str(result)
print (msg)