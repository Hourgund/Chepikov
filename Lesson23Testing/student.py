class Student:

    def __init__(self):
        self.name = "no name"
        self.age = 16
        self.mark = 4


#      print("Calling defoult-costructor")


def init(st, name, age, mark):
    st.name = name
    st, age = age
    st.mark = mark
