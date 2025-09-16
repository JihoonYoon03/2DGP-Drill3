from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')


def move_bottom():
    pass


def move_right():
    pass


def move_top():
    pass


def move_left():
    pass


def move_rectangle():
    x, y = 400, 90
    move_bottom()
    move_right()
    move_top()
    move_left()
    draw_everything(x, y)
    pass


def draw_everything(x: int, y: int):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.05)


def move_triangle():
    pass


def move_circle():
    pass


while True:
    move_rectangle()
    move_triangle()
    move_circle()
    # break
    pass

close_canvas()
