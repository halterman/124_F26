import turtle

previous_x = 1000
previous_y = 1000

def draw_circle(x: float, y: float) -> None:
    global previous_x, previous_y
    turtle.color('blue')
    if previous_x < 1000:
        turtle.pensize(5)
        turtle.teleport(x, y)
        turtle.goto(previous_x, previous_y)
    turtle.teleport(x, y - 25)
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.update()

    previous_x = x
    previous_y = y

def do_mouse_click(x: float, y: float) -> None:
    print(f'x = {x}, and y = {y}')
    # draw_square(x, y)
    draw_circle(x, y)

def draw_square(x: float, y: float) -> None:
    turtle.teleport(x - 25, y - 25)
    turtle.setheading(0)
    turtle.color('red')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    turtle.update()

turtle.title('Connect the circles')
screen = turtle.Screen()
screen.onscreenclick(do_mouse_click)
turtle.hideturtle()
turtle.tracer(0)
turtle.speed(0)
screen.mainloop()