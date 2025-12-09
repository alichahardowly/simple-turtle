import turtle
import time

t = turtle.Turtle()
t.speed(3)
t.pensize(4)

screen = turtle.Screen()
screen.setup(width=900, height=500)
screen.bgcolor("white")
t.penup()
t.goto(250, 50)
t.pendown()

# تابع برای حرکت روان
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#############################
# نوشتن "علی"
#############################




# ع (نسخه ساده‌شده)
move_to(150, 50)
t.circle(-30, -180)
t.forward(80)
# ل
move_to(70, -10)
t.right(90)
t.forward(170)
# ی
move_to(70, -10)
t.right(90)
t.forward(-50)
t.right(30)
t.forward(50)
t.left(60)
t.forward(-20)
t.backward(60)
t.right(-30)
t.right(-90)
t.forward(70)
t.right(90)
t.forward(70)
turtle.done()