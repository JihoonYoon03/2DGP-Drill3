import math
from pico2d import *

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

def draw_everything(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    """사각형 운동 - 중앙하단 -> 우하단 -> 우상단 -> 좌상단 -> 좌하단 -> 중앙하단 (시계 방향)"""
    # 캐릭터가 화면 밖으로 나가지 않도록 경계 설정 (캐릭터 크기 고려)
    left = 50
    right = 750
    bottom = 90
    top = 550
    center_x = 400

    # 1. 중앙하단 -> 우하단
    y = bottom
    for x in range(center_x, right + 1, 5):
        draw_everything(x, y)

    # 2. 우하단 -> 우상단
    x = right
    for y in range(bottom, top + 1, 5):
        draw_everything(x, y)

    # 3. 우상단 -> 좌상단
    y = top
    for x in range(right, left - 1, -5):
        draw_everything(x, y)

    # 4. 좌상단 -> 좌하단
    x = left
    for y in range(top, bottom - 1, -5):
        draw_everything(x, y)

    # 5. 좌하단 -> 중앙하단 (시작점으로 돌아가기)
    y = bottom
    for x in range(left, center_x + 1, 5):
        draw_everything(x, y)

def move_triangle():
    """삼각형 운동 - 중앙하단 -> 우하단 -> 중앙상단 -> 좌하단 -> 중앙하단 (시계 방향)"""
    center_bottom_x, center_bottom_y = 400, 90
    right_bottom_x, right_bottom_y = 750, 90
    center_top_x, center_top_y = 400, 550
    left_bottom_x, left_bottom_y = 50, 90

    # 1. 중앙 하단에서 우측 하단으로
    steps = 70
    delX = (right_bottom_x - center_bottom_x) / steps
    delY = (right_bottom_y - center_bottom_y) / steps

    x, y = center_bottom_x, center_bottom_y
    for i in range(steps):
        draw_everything(int(x), int(y))
        x += delX
        y += delY

    # 2. 우측 하단에서 중앙 상단으로
    delX = (center_top_x - right_bottom_x) / steps
    delY = (center_top_y - right_bottom_y) / steps

    x, y = right_bottom_x, right_bottom_y
    for i in range(steps):
        draw_everything(int(x), int(y))
        x += delX
        y += delY

    # 3. 중앙 상단에서 좌측 하단으로
    delX = (left_bottom_x - center_top_x) / steps
    delY = (left_bottom_y - center_top_y) / steps

    x, y = center_top_x, center_top_y
    for i in range(steps):
        draw_everything(int(x), int(y))
        x += delX
        y += delY

    # 4. 좌측 하단에서 중앙 하단으로 돌아가기
    delX = (center_bottom_x - left_bottom_x) / steps
    delY = (center_bottom_y - left_bottom_y) / steps

    x, y = left_bottom_x, left_bottom_y
    for i in range(steps):
        draw_everything(int(x), int(y))
        x += delX
        y += delY

def move_circle():
    """원 운동 - 중앙 하단에서 시작해서 시계 방향으로 회전"""
    center_x, center_y = 400, 320
    radius = 200

    # 중앙 하단에서 시작하도록 각도 조정 (270도에서 시작)
    # 시계 방향으로 회전하도록 각도를 감소시킴
    for angle in range(270, 270 - 360, -3):
        radian = math.radians(angle)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
        draw_everything(x, y)

def main():
    """메인 실행 함수 - 사각형 -> 삼각형 -> 원형 순서로 반복"""
    while True:
        # 1. 사각형 운동
        move_rectangle()

        # 2. 삼각형 운동 (사각형과 원형 사이에 추가)
        move_triangle()

        # 3. 원형 운동
        move_circle()

if __name__ == "__main__":
    main()
    close_canvas()
