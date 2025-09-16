from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')


def move_bottom_left():
    for x in range(20, 400, 5):
        draw_everything(x, 90)
    pass

def move_bottom_right():
    pass


def move_right():
    pass


def move_top():
    pass


def move_left():
    pass


def move_rectangle():
    move_bottom_right()
    move_right()
    move_top()
    move_left()
    move_bottom_left()
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
