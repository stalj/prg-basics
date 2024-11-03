import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5) 

figures.pen_move(100, 50)

figures.draw_rectangle(100, 50)

figures.pen_move(200, 100)

figures.draw_triangle(60)

figures.pen_move(-200, -30)

figures.draw_rectangle(100, 100)

pen.hideturtle()
window.mainloop()