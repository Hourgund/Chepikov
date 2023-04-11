class Student:

    def __init__(self, name, age, mark):
        print("Calling costructor with arguments")
        self.name = name
        self.age = age
        self.mark = mark


#      print("Calling defolt-costructor")


def init(st, name, age, mark):
    st.name = name
    st.age = age
    st.mark = mark
