from random import randrange

#randrange(5) -- > {0 1 2 3 4}

#range(5) --> [0,1,2,3,4]
#range(2,5)--> [2,3,4]
#range(2,15,2) --> [2 4 6 8 10 12 14]

# container = range(5)
# print(type(container))

for value in range(5, 100, 5):
    print(value, end=' ')