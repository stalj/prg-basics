import turtle

pen = turtle.Turtle()
pen.speed(5)  

def draw_triangle(side_len):

    for i in range(3):
        pen.forward(side_len)
        pen.right(120)


def draw_rectangle(side_len1, side_len2):

    for i in range(2):
        pen.forward(side_len1)
        pen.right(90)
        pen.forward(side_len2)
        pen.right(90)

def pen_move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()