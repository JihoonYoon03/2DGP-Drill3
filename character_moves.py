from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')


def move_bottom_left():
    for x in range(20, 400, 5):
        draw_everything(x, 90)

def move_bottom_right():
    for x in range(400, 780, 5):
        draw_everything(x, 90)


def move_up():
    for y in range(90, 560, 5):
        draw_everything(780, y)


def move_top():
    for x in range(780, 20, -5):
        draw_everything(x, 560)


def move_down():
    for y in range(560, 90, -5):
        draw_everything(20, y)


def move_rectangle():
    move_bottom_right()
    move_up()
    move_top()
    move_down()
    move_bottom_left()


def draw_everything(x: int, y: int):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.05)


def move_tri_up():
    x = 780
    y = 90
    delX = 5
    delY = 470 / (380 / delX)

    while x > 400 and y < 560:
        draw_everything(x, y)
        x -= delX
        y += delY


def move_tri_down():
    x = 400
    y = 560
    delX = 5
    delY = 470 / (380 / delX)

    while x > 20 and y > 90:
        draw_everything(x, y)
        x -= delX
        y -= delY


def move_triangle():
    move_bottom_right()
    move_tri_up()
    move_tri_down()
    move_bottom_left()


def move_circle():
    pass


while True:
    # move_rectangle()
    move_triangle()
    move_circle()
    # break
    pass

close_canvas()
