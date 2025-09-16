from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def move_rectangle():
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
