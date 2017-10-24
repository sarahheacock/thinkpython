import math

print "Hello, World!"

x = y = 1
r = 5


print(x, y)
print x, y
print(math.pi)
print(4 * math.pi * 5**3 / 3)
print 4 * math.pi * 5**3 / 3

# chapter 2 ======================================================
books = 60
price = 24.95
discount = 0.4
first = 3
rest = 0.75

print(books * ((1 - discount) * price + rest) + (first - rest))


start = (6 * 60 + 52) * 60
easy = 8 * 60 + 15
quantEasy = 2
fast = 2 * 60 + 12
quantFast = 3

total = start + quantEasy * easy + quantFast * fast
hours = total/3600.0
floored = total//3600
minutes = (hours - floored)*60

print '%d:%d' % (hours, minutes)


# chapter 3 ======================================================
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

print(print_lyrics) # <function print_lyrics at 0x10c244938>
repeat_lyrics() # I'm .... I'm ....

def right_justify(string):
    print ' ' * (70 - len(string)) + string

right_justify('monty')
right_justify("eghjklfghjk")

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def printRow():
    string = " +" + " -" * 4
    print(string * 2 + " +")

def printCol():
    string = " |" + " " * 8
    print(string * 2 + " |")

def create():
    printRow()
    do_four(printCol)

def final():
    do_twice(create)
    printRow()

final()

