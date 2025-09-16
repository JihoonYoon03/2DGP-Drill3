from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')


def move_bottom():
    pass


def move_up():
    pass


def move_top():
    pass


def move_down():
    pass


def move_rectangle():
    move_bottom()
    move_up()
    move_top()
    move_down()
    clear_canvas_now()
    boy.draw_now(400, 90)
    grass.draw_now(400, 30)
    delay(0.05)
    pass


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
