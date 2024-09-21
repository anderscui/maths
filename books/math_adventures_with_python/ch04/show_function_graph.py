# coding=utf-8
xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    global xscl, yscl
    size(600, 600)

    # width and height are set in `setup`
    xscl = width / rangex
    # default layout: upside-down
    yscl = - height / rangey
    print('width and height:', width, height)
    print('xscl and yscl:', xscl, yscl)


# def f(x):
#    return x ** 2 - 1

def f(x):
    return 6 * x ** 3 + 31 * x ** 2 + 3 * x - 10


def graph_f():
    x = xmin
    step = 0.1
    while x <= xmax:
        fill(0)
        y = f(x)
        next_x = x + step
        next_y = f(next_x)
        line(x * xscl, y * yscl, next_x * xscl, next_y * yscl)
        x += step


def draw():
    global xscl, yscl
    background(255)

    # move origin from the top left to the center of the screen
    translate(width / 2, height / 2)
    # set line thickness
    strokeWeight(1)
    # set line color
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        # for line(), set coordinates for begin and end points.
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)

    # axes
    stroke(0, 127, 127)
    line(0, ymin * yscl, 0, ymax * yscl)
    line(xmin * xscl, 0, xmax * xscl, 0)

    fill(0)

    # ellipse(3 * xscl, 6 * yscl, 10, 10)
    graph_f()
