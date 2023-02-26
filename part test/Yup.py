import pygame
import pygame as py
import random as ri

pygame.init()
screen = pygame.display.set_mode()
xsc, ysc = screen.get_size()
x, y = screen.get_size()  # for player
w, h = x // 2, y // 2
razmetka_y = ysc // 8
gran = xsc // 6  # для отрисовки меню
clock = pygame.time.Clock()
collor_circle = (255, 255, 255)
color_triangle = (255, 255, 255)
color_rect = (255, 255, 255)
# images
st_sc = pygame.image.load('../Shablons/image/продам гараж.jpg')
st_sc = pygame.transform.scale(st_sc, (xsc, ysc))
blop = pygame.transform.scale(pygame.image.load('../Shablons/image/blop.png'), (gran, xsc))
xscr, yscr = screen.get_size()
wpls = 300 * 1.7
py.mixer.music.load('../sounds/shum.mp3')
xlogo = 0
# image init
pls_use_hd = py.image.load('../image/please.jpg')
pls_use_hd = py.transform.scale(pls_use_hd, (wpls, wpls // 1.7))
pls_use_hd.set_alpha(2)
logo_rote = py.image.load('../image/logo.png')
logo_rote = py.transform.scale(logo_rote, (100, 100))
lim = 0
pygame.mouse.set_visible(False)
for i in range(255):
    pls_use_hd.set_alpha(i)
    pygame.time.delay(50)
    screen.blit(pls_use_hd, (xscr // 2 - wpls // 2, yscr // 2 - 150))
    py.display.update()
screen.fill((0, 0, 0))
py.mixer.music.play(-1)
for i in range(xscr // 2 - 50):
    screen.fill((0, 0, 0))
    xlogo += 1
    screen.blit(logo_rote, (xlogo, yscr // 2 - 50))
    py.display.update()
pygame.time.delay(2000)


def start_screen():
    global color_triangle, collor_circle, color_rect, stsc, ms
    pos = pygame.mouse.get_pos()
    dfig = gran // 2  # for figures center
    yg = ysc // 6
    width = 5
    screen.blit(st_sc, (0, 0))  # типо главного экрана
    # pygame.draw.rect(screen, (0, 0, 0), (0, 0, gran, xsc))  # отрисовка меню
    screen.blit(blop, (0, 0))
    pygame.draw.line(screen, (255, 255, 255, 50), (gran, 0), (gran, ysc), 4)  # Полоска заканчивающая первый уровень меню
    # exit(rect)
    len_rect = gran // 4
    pygame.draw.rect(screen, color_rect, (dfig - yg // 2, yg * 4.5, yg, yg), width)
    pygame.draw.rect(screen, color_rect, (dfig - yg // 2 + 15, yg * 4.5+ 15, yg, yg), width)
    pygame.draw.line(screen, color_rect, (dfig - yg // 2, yg * 4.5), (dfig * 1.5 + 4 + 15, yg * 5.5 + 15), 4)
    #pygame.draw.line(screen, (0,255,0), (dfig - yg // 2, yg * 5.5), (dfig * 1.5 + 4, yg * 4.5), 4)
    # settings(circle)
    pygame.draw.rect(screen, collor_circle, (dfig - yg // 2, y // 2 - 15, yg, 30), width)
    pygame.draw.rect(screen, collor_circle, (gran // 2 - 15, yg * 2.5, 30, yg), width)

    pygame.draw.rect(screen, color_triangle, (dfig - yg // 2, y // 6, yg, 30), width)
    if dfig - yg // 2 <= pos[0] <= dfig + yg // 2:
        if yg // 1.5 <= pos[1] <= yg * 1.5:
            color_triangle = (45, 255, 45)
            if pygame.mouse.get_pressed()[0]:
                stsc = False
        elif yg * 2.5 <= pos[1] <= yg * 3.5:
            collor_circle = (45, 255, 45)
            if pygame.mouse.get_pressed()[0]:
                print('hasnt in this version')
                pygame.time.delay(150)
        elif yg * 4.5 <= pos[1] <= yg * 5.5:
            color_rect = (45, 255, 45)
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            collor_circle = (255, 255, 255)
            color_triangle = (255, 255, 255)
            color_rect = (255, 255, 255)
            pygame.mixer.music.play(1)


py.mouse.set_visible(1)
pygame.mixer.music.load("../sounds/choice.mp3")
stsc = True
while stsc:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    start_screen()
    pygame.display.update()
screen.fill((255, 255, 255))
