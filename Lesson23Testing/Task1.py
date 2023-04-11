from student import Student
from manager import Manager


# def main():
#    st1 = Student("Alex", 20, 10)
#    st2 = Student("Kate", 18, 7)
#    st3 = Student("Peter", 21, 9)
#    st4 = Student()


#    init(st1, "Alex", 20, 10)
#    init(st1, "Kate", 18, 9)

#    st1.name = "Alex"
#    st2.name = "Anna"
#    st1.mark = 10
#    st2.mark = 7
#    st1.age = 20
#    st2.age = 18

#    print(st1.name)
#    print(getattr(st1, "name"))
#    print(st1.__getattribute__("name"))

#    del st1.name
#    delattr(st1, "mark")
#    st1.__delattr__("age")

#    st1.name = "Alex"
#   setattr(st1, "name", "Peter")
#    st1.__setattr__("name", "Olya")

#   print(vars(st1))


#    print(st1.__dict__)
#    print(dir(st1))
#    print(help(st1))
def main():
    manager = Manager()
    s1 = Student("Alex", 20, 10)
    s2 = Student("Kate", 18, 9)
    s3 = Student("Peter", 22, 5)

    ls = [s1, s2, "abc", s3, 5]

    result = manager.calc_avg_mark(ls)

    print(f"Result is {result}.")


if __name__ == '__main__':
    main()
