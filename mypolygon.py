import turtle
import math

def square(t, length): 
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle): 
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    num = 360
    # length = math.pi * 2 * r / num
    arc(t, r, num)

def triangle(t, n, l):
    largeAngle = 360.0/n
    smallAngle = 180 - (180.0 - largeAngle) / 2
    smallSide = l / (2 * math.sin(math.radians(largeAngle/2)))

    print(largeAngle, smallAngle, smallSide)

    t.fd(l)
    t.lt(smallAngle)
    t.fd(smallSide)
    t.lt(180 - largeAngle)
    t.fd(smallSide)
    # back to start
    t.lt(smallAngle)
    t.fd(l)
    t.lt(largeAngle)



def pie(t, n):
    for j in range(n):
        triangle(t, n, 50)


def flower(t, n):
    step_angle = 360.0/n
    for i in range(n):
        arc(t, 50, step_angle)
        t.lt(step_angle * 2)
        t.rt(180)

        arc(t, 50, step_angle)
        t.lt(step_angle)
        #t.rt(step_angle)

bob = turtle.Turtle()
# square(bob, 100)
# square(bob, 50)
# polygon(bob, 100, 5)
# polygon(bob, 100, 6)
flower(bob, 5)


turtle.mainloop()