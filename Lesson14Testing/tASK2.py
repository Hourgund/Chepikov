NUMBER_OF_STUDENTS = 5


def calc_mark_avg(mark1, mark2, mark3, mark4, mark5):
    if 10 < mark1 <= 0 and 10 < mark2 <= 0 and 10 < mark1 <= 0:
        return "Invalid value! Try again."

    s = mark1
    s += mark2
    s += mark3
    s += mark4
    s += mark5

    return s / NUMBER_OF_STUDENTS


def main():
    mark1 = int(input("Mark of first student: "))
    mark2 = int(input("Mark of second student: "))
    mark3 = int(input("Mark of third student: "))
    mark4 = int(input("Mark of forth student: "))
    mark5 = int(input("Mark of fifth student: "))

    avg_mark = calc_mark_avg(mark1, mark2, mark3, mark4, mark5)
    avg_mark = round(avg_mark, 1)

    msg = f"Group average mark is {avg_mark}"

    print(msg)


if __name__ == "__main__":
    main()
