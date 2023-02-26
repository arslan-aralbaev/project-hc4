import pygame
import pygame as py
pygame.init()
x = 1200
y = 600
speed = 1
q = x // 2
w = y // 2
pygame.mixer.init()
screen = pygame.display.set_mode((x, y))
pygame.display.update()
state = py.transform.scale(py.image.load('../image/stare.png'), (60, 87))
up = py.transform.scale(py.image.load('../image/up.png'), (60, 87))
down = py.transform.scale(py.image.load('../image/down.png'), (60, 87))
univer = py.transform.scale(py.image.load('../image/univer.png'), (60, 87))
user = state
speed = 2
tick = 0
while True:
    tick += 1
    screen.fill((0, 0, 0))
    if tick % 10 >= 5:
        user = up
    else:
        user = down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        if keys[pygame.K_LEFT]:
            q -= speed
        elif keys[pygame.K_RIGHT]:
            q += speed

        if keys[pygame.K_UP]:
            w -= speed
        elif keys[pygame.K_DOWN]:
            w += speed
    else:
        user = state
    if q == x:
        q = 0
    elif q == 0:
        q = x
    elif y == w:
        w = 0
    elif w == 0:
        w = y
    screen.blit(user, (q, w))
    pygame.display.update()
    pygame.time.delay(20)
