import turtle as t
from itertools import cycle

colors = cycle(['red', 'green', 'orange', 'yellow', 'blue', 'purple'])

bg_colors = cycle(['Purple', 'Peru', 'Forest Green', 'goldenrod', 'Hot pink' ])


def draw_shape(size, angle, shift, shape):
    #t.bgcolor(next(bg_colors))
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size * 2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(shift)
    draw_shape(size + 5, angle + 1, shift + 1, next_shape)
    
    
t.bgcolor('black')
t.speed('fast')
t.pensize(20)

draw_shape(30, 0, 1, 'circle')


