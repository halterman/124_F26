import turtle

def do_mouse_click(x: float, y: float) -> None:
    print(f'x = {x}, and y = {y}')
    draw_square(x, y)

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

screen = turtle.Screen()
screen.onscreenclick(do_mouse_click)
turtle.hideturtle()
turtle.tracer(0)
turtle.speed(0)
screen.mainloop()