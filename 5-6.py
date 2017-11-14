import turtle

def draw(t, length):
    if length < 3:
        t.fd(length)
    else:
        draw(t, length / 3)
        t.lt(60)
        draw(t, length / 3)
        t.rt(120)
        draw(t, length / 3)
        t.lt(60)
        draw(t, length / 3)

def snowFlake(t, length):
    for i in range(3):
        draw(t, length)
        t.rt(120)


bob = turtle.Turtle()
snowFlake(bob, 200)
turtle.mainloop()
