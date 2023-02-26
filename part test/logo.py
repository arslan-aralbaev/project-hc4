import pygame
import pygame as py
import time
py.init()
screen = py.display.set_mode()
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
while True:
    screen.fill((0, 0, 0))
    for i in py.event.get():
        if i.type == py.QUIT:
            exit()
    py.display.update()