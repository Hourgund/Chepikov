a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

exist = all((a + b > c, b + c > a, c + a > b))

result = exist and (a**2 + b**2 == c**2
                    or a**2 + c**2 == b**2
                    or c**2 + b**2 == a**2)

# msg = "Can this triangle be right angled?"
# msg += "\nAnswer: " + str(result)

msg = "Is the triangle right angled?"
msg += "\n" + ("Yes, the triangle is right angled."
               if result else "No, the triangle isn't right angled.")

print(msg)