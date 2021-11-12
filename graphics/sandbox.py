import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

#Foot
t.goto(-100, -150)
rectangle(50, 20, 'Blue')

t.goto(-30, -150)
rectangle(50, 20, 'Blue')


#Legs

t.goto(-25, -50)
rectangle(15, 100, 'Red')

t.goto(-55, -50)
rectangle(-15, 100, 'Red')

#Body
t.goto(-90, 100)
rectangle(100, 150, 'Forest Green')

#Hands
#left
t.goto(-150, 70)
rectangle(60, 15, 'Peru')
t.goto(-150, 110)
rectangle(15, 40, 'Peru')

#right
t.goto(10, 70)
rectangle(60, 15, 'Peru')
t.goto(55, 110)
rectangle(15, 40, 'Peru')

#Neck
t.goto(-50, 120)
rectangle(15, 20, 'Grey')

#Head
t.goto(-85, 170)
rectangle(80, 50, 'Goldenrod')

#Eyes
t.goto(-60, 160)
rectangle(30, 10, 'White')

#Mouth
t.goto(-65, 135)
rectangle(40, 5, 'Black')

#left eye
t.goto(-55, 155)
rectangle(5, 5, 'Black')

#right eye
t.goto(-40, 155)
rectangle(5, 5, 'Black')
