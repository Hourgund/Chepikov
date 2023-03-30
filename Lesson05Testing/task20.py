# 24 --> True
# 12 --> False
# 11 --> False
# 99 --> False
# 10 --> False
# 20 --> True

number = int(input('Input your number: '))

a = number % 10
b = number // 10
result = (a % 2 == 0) and (b % 2 == 0)

msg = "Has " + str(number) + "all digits even?"
msg += "\nAnswer: " + str(result)

# print ('Has ', number, 'all digits even?')
# print ("Answer: ", result)

print(msg)