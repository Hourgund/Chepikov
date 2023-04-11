from student import Student


def main():
    st1 = Student()
    st2 = Student()

    st1.name = "Alex"
    st2.name = "Anna"
    st1.mark = 10
    st2.mark = 7
    st1.age = 20
    st2.age = 18

    print(st1.name)
    print(getattr(st1, "name"))

    print(vars(st1))


if __name__ == '__main__':
    main()
