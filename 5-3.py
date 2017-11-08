# take in 3 lengths output if triangle can be made

def is_triangle():
    a = int(raw_input('side one:\n')) #largest side

    b = int(raw_input('side one:\n'))
    if b > a :
        temp = a
        a = b
        b = temp

    c = int(raw_input('side one:\n'))
    if c > a :
        temp = a
        a = c
        c = temp

    if a < b + c :
        print("yes")
    else :
        print("no")

is_triangle()
