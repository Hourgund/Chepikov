age = int(input("Whats your age? "))
days = int(input("How many days past after your birthday? "))

month = age * 12
week = age * 54
day = (age * 356) + days
hour = day * 24
minute = hour * 60
second = minute * 60
millisecond = second * 1000

print("Age:", age)
print("Month:", month)
print("Weeks:", week)
print("Days:", day)
print("Hours:", hour)
print("Minute:", minute)
print("Second:", second)
print("Millisecond:", millisecond)