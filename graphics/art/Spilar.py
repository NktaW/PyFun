import turtle as t
from itertools import cycle

colors = cycle(['red', 'green', 'orange', 'yellow', 'blue', 'purple'])

bg_colors = cycle(['Purple', 'Peru', 'Forest Green', 'goldenrod', 'Hot pink' ])


def draw_circle(size, angle, shift):
    t.bgcolor(next(bg_colors))
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 10, angle + 10, shift + 1)
    
    
t.bgcolor('black')
t.speed('fast')
t.pensize(20)

draw_circle(30, 0, 1)


