import pygame as py

py.init()
screen = py.display.set_mode()
x, y = screen.get_size()
m, k = x // 2, y // 4
clr = (255, 0, 0)


def krest():
    global m, k, clr
    py.draw.rect(screen, (255, 255, 255), (0, 0, x / 2, x / 2), 0)
    py.draw.rect(screen, (255, 0, 0), (x / 6 * 2, 0, x / 6, x / 2))
    py.draw.rect(screen, (0, 255, 0), (0, x / 6 * 2, x / 2, x / 6))
    py.draw.rect(screen, (0, 0, 255), (0, 0, x / 6, x / 2))
    py.draw.rect(screen, (0, 255, 255), (0, 0, x / 3, x / 6))
    if py.mouse.get_pressed()[0]:
        clr = (0, 255, 0)
        pos = py.mouse.get_pos()
        if 1:
            k += -1
        '''if 0 <= pos[0] <=x/4 and 0 <= pos[1] <= y:
            m -= 1
        if 0 <= pos[0] <= x and y - y/4 <= pos[1] <= y:
            k += 1
        if x - x/4 <= pos[0] <= x and 0 <= pos[1] <= y:
            m += 1'''
        py.draw.circle(screen, clr, (pos[0], k), 10, 0)


while True:
    screen.fill((0, 0, 0))

    clr = (255, 0, 0)
    krest()

    py.display.update()