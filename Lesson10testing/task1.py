# Roman Numerals (Римские цифры)
# Напишите программу, которая считывает целое число и выводит
# соответствующую ему римскую цифру. Если число находится вне
# диапазона 1-10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.
# Число Римская цифра
# 1 	I
# 2 	II
# 3 	III
# 4 	IV
# 5 	V
# 6 	VI
# 7 	VII
# 8 	VIII
# 9 	IX
# 10 	X

def number(n):
    if not (1 <= n <= 10):
        return "Wrong Data"

    msg = "X"

    if n <= 3:
        msg = "I" * n
    elif n == 4:
        msg = "IV"
    elif n <= 8:
        msg = "V" + "I" * (n - 5)
    elif n == 9:
        msg = "IX"

    return msg


def main():
    n = int(input("Input your number from 1 to 10: "))
    msg = number(n)
    print(msg)


def testing():
    result = " 1 --> I : " + str(number(1) == "I")
    result += "\n 2 --> II : " + str(number(2) == "II")
    result += "\n 3 --> III : " + str(number(3) == "III")
    result += "\n 4 --> IV : " + str(number(4) == "IV")
    result += "\n 5 --> V : " + str(number(5) == "V")
    result += "\n 6 --> VI : " + str(number(6) == "VI")
    result += "\n 7 --> VII : " + str(number(7) == "VII")
    result += "\n 8 --> VIII : " + str(number(8) == "VIII")
    result += "\n 9 --> IX : " + str(number(9) == "IX")
    result += "\n 10 --> X : " + str(number(10) == "X")

    result += "\n 0 --> Error : " + str(number(0) == "Wrong Data")
    result += "\n 100 --> Error : " + str(number(100) == "Wrong Data")

    print(result)


testing()
main()
