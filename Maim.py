import random
import pygame
import pygame as py
from random import randint as ri

pygame.init()
screen = pygame.display.set_mode()
global_time = (0, 0)
xsc, ysc = screen.get_size()
x = 160
y = 190
x_ghost, y_ghost = xsc, ysc
q_last, w_last = x, y
razmetka_y = ysc // 8
gran = xsc // 6  # для отрисовки меню
clock = pygame.time.Clock()
collor_circle = (255, 255, 255)
color_triangle = (255, 255, 255)
color_rect = (255, 255, 255)
font = pygame.font.SysFont('arial', 15)
walls_point = list()
boxes_point = list()
walls_array = list()
debugText = ''
debugPoint = 1
lifeTarget = 'monster'
death_const = False
keys_color = ['red', 'green', 'yellow', 'blue', 'fantom']
file = open('source/level_1.lvl', mode='r')

st_sc = pygame.image.load('image/fogs.png')
st_sc = pygame.transform.scale(st_sc, (xsc, ysc))
blop = pygame.transform.scale(pygame.image.load('image/menu.png'), (gran, xsc))
xscr, yscr = screen.get_size()
wpls = 300 * 1.7
py.mixer.music.load('sounds/shum.mp3')
xlogo = 0
wlayer, hayeler = 40, 67
users_puls = 72
stsc = True
bottle_png = py.transform.scale(py.image.load('image/bottle.png'), (11, 11 * 3))
pls_use_hd = py.image.load('image/please.jpg')
pls_use_hd = py.transform.scale(pls_use_hd, (wpls, wpls // 1.7))
pls_use_hd.set_alpha(2)
logo_rote = py.image.load('image/logo.png')
logo_rote = py.transform.scale(logo_rote, (100, 100))
darkness = py.transform.scale(py.image.load('image/fog.png'), (xsc * 2, ysc * 2))
fogs = py.image.load('image/fogs.png')
state = py.transform.scale(py.image.load('image/stare.png'), (wlayer, hayeler))
up = py.transform.scale(py.image.load('image/up.png'), (wlayer, hayeler))
down = py.transform.scale(py.image.load('image/down.png'), (wlayer, hayeler))
univer = py.transform.scale(py.image.load('image/univer.png'), (wlayer, hayeler))
lvl2 = py.transform.scale(py.image.load('image/lvl2.png'), (xsc, ysc))
box = py.transform.scale(py.image.load('image/box.png'), (70, 70))
chastota_bienie = 1
user = state
user_visible = True
pygame.mouse.set_visible(False)
'''
for i in range(255):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pls_use_hd.set_alpha(i)
    pygame.time.delay(50)
    screen.blit(pls_use_hd, (xscr // 2 - wpls // 2, yscr // 2 - 150))
    py.display.update()
screen.fill((0, 0, 0))
py.mixer.music.play(-1)
for i in range(xscr // 2 - 50):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0, 0, 0))
    xlogo += 1
    screen.blit(logo_rote, (xlogo, yscr // 2 - 50))
    py.display.update()
pygame.time.delay(2000)
'''


class Hidden_box:
    def __init__(self, start, side=70):
        self.x_start = start[0]
        self.y_start = start[1]
        self.width = side
        self.height = side

    def draw(self):
        global keys, user_visible, ghost_yarik, lifeTarget
        if (self.x_start, self.y_start, self.x_start + self.width, self.y_start + self.height) in boxes_point:
            screen.blit(box, (self.x_start, self.y_start))
            if keys[pygame.K_e] and any(points_check(x, y, boxes_point)):
                user_visible = False
                lifeTarget = 'walker'
            else:
                lifeTarget = 'monster'
        else:
            boxes_point.append((self.x_start, self.y_start, self.x_start + self.width, self.y_start + self.height))


class Key:
    def __init__(self, score):
        if x > 10 and y > 10:
            self.x = random.randint(10, x - 30)
            self.y = random.randint(10, y - 30)
            self.score = score
            self.color = random.choice(keys_color)
            keys_color.pop(keys_color.index(self.color))

    def draw(self):
        if x <= self.x <= x + 40 and \
                y <= self.y <= y + 67:
            self.score += 1
            py.time.delay(10)
            self.x = self.y = xsc + ysc
            print('bottle')
        screen.blit(bottle_png, (self.x, self.y))


def exist():
    for hl in pygame.event.get():
        if hl.type == pygame.QUIT:
            exit()


def debugInfo(msg):
    global debugText
    debugSurf = py.Surface((xsc // 3, ysc * 0.7))
    debugSurf.set_alpha(120)
    debugText = msg
    # player possition
    py.draw.line(screen, (255, 0, 0), (0, y + hayeler / 2), (xsc, y + hayeler / 2), 1)
    py.draw.line(screen, (255, 0, 0), (x + wlayer / 2, 0), (x + wlayer / 2, ysc), 1)
    py.draw.rect(screen, (147, 2, 255), (x, y, wlayer, hayeler), 2)
    # ghost possition
    py.draw.line(screen, (255, 0, 0), (0, y_ghost + hayeler / 2), (xsc, y_ghost + hayeler / 2), 1)
    py.draw.line(screen, (255, 0, 0), (x_ghost + wlayer / 2, 0), (x_ghost + wlayer / 2, ysc), 1)
    py.draw.rect(screen, (147, 2, 255), (x_ghost, y_ghost, wlayer, hayeler), 2)
    text = font.render(debugText, True, (232, 150, 40))
    debugSurf.blit(text, (10, 10))
    screen.blit(debugSurf, (5, 5))


# ##################################Начало отвратительной части кода, чтобы не использовать


def context_menu(x_top, y_top):
    screen.fill((0, 0, 0))
    py.draw.rect(screen, (255, 0, 0), (x_top, y_top, x_top + 100, y_top + 100), 24)
    py.display.update()


class Pause:
    def __init__(self):
        self.x_window = (x // 2) - 100
        self.y_window = -100

    def open(self, key):
        while True:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                break
            if self.y_window < 100:
                self.y_window += 1
                context_menu(self.x_window, self.y_window)
            exist()
        while self.y_window > -100:
            self.y_window -= 1
            context_menu(self.x_window, self.y_window)


# ##################################Конец отвратительной части кода, чтобы не использовать


class Mob:
    def __init__(self, x_pik, y_pik, speed_up, target, side_up, side_down, side_crash):
        self.x = x_pik
        self.y = y_pik
        self.y_speed = speed_up
        self.x_speed = speed_up
        self.target = target
        self.gluk = py.image.load(side_crash)
        self.side_move = py.image.load(side_up)
        self.side_stay = py.image.load(side_down)
        self.targetx = ri(10, xsc)
        self.targety = ri(10, ysc)
        self.relax = 0
        self.flag = True
        self.frst = self.side_stay
        self.tws = self.side_move
        self.character = self.tws

    def live(self, target):
        global x, y, x_ghost, y_ghost, lifeTarget
        self.target = lifeTarget
        x_ghost, y_ghost = self.x, self.y
        if self.target == 'monster':
            self.targetx, self.targety = x, y
            if sum(points_check(self.x, self.y, [(x, y, x + wlayer, y + hayeler)])) and user_visible:
                exit()  # scrimer on another die animation 'dr1'
        if self.targetx - 5 <= self.x <= self.targetx + 5 and \
                self.targety - 5 <= self.y <= self.targety + 5 and self.target == 'walker':
            if self.flag:
                self.relax = int(global_time[0])
                self.flag = False
            if self.relax + 10 >= int(global_time[0]):
                self.targetx = ri(10, xsc)
                self.targety = ri(10, ysc)
                self.flag = True
            self.frst, self.tws = self.side_stay, self.side_stay
        if int(global_time[1]) % 2 == 0:
            self.character = self.frst
        else:
            self.character = self.tws
        if self.targety > self.y:
            self.y_speed = 1
        else:
            self.y_speed = -1
        if self.targetx > self.x:
            self.x_speed = 1
            self.frst = py.transform.flip(self.side_stay, True, False)
            self.tws = py.transform.flip(self.side_move, True, False)
        elif self.targetx < self.x:
            self.x_speed = -1
            self.frst, self.tws = self.side_move, self.side_stay
        self.x += self.x_speed
        self.y += self.y_speed
        screen.blit(self.character, (self.x, self.y))


def start_screen():
    global color_triangle, collor_circle, color_rect, stsc
    py.mouse.set_visible(True)
    dfig = gran // 2  # for figures center
    yg = ysc // 6
    width = 5
    screen.blit(st_sc, (0, 0))  # аставка главного экрана
    screen.blit(blop, (0, 0))  # затемнение
    # exit button
    pygame.draw.line(screen, (255, 255, 255, 50), (gran, 0), (gran, ysc), 4)  # Полоска первого уровеня меню
    pygame.draw.rect(screen, color_rect, (dfig - yg // 2, yg * 4.5, yg, yg), width)
    pygame.draw.rect(screen, color_rect, (dfig - yg // 2 + 15, yg * 4.5 + 15, yg, yg), width)
    pygame.draw.line(screen, color_rect, (dfig - yg // 2, yg * 4.5), (dfig * 1.5 + 4 + 15, yg * 5.5 + 15), 4)
    pygame.draw.line(screen, (0, 255, 0), (dfig - yg // 2, yg * 5.5), (dfig * 1.5 + 4, yg * 4.5), 4)
    # settings button
    pygame.draw.rect(screen, collor_circle, (dfig - yg // 2, (ysc // 2) - 15, yg, 30), width)
    pygame.draw.rect(screen, collor_circle, (gran // 2 - 15, yg * 2.5, 30, yg), width)
    # start button
    pygame.draw.rect(screen, color_triangle, (dfig - yg // 2, (ysc // 2) // 3, yg, 30), width)
    pos = pygame.mouse.get_pos()
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


def points_check(x_now, y_now, df_point):
    side = [False, False, False, False]  # AB BC CD DA
    if df_point:
        for point in df_point:
            if point[0] < x_now < point[2] + 5:
                if point[1] < y_now < point[3] or point[1] < y_now + hayeler < point[3] or\
                   point[1] < y_now + hayeler // 2 < point[3] or point[1] < y_now + hayeler < point[3]:
                    side[0] = True
            if point[1] < y_now < point[3] + 5:
                if point[0] < x_now < point[2] or point[0] < x_now + wlayer < point[2] or\
                   point[0] < x_now + wlayer // 2 < point[2] or point[0] < x_now + wlayer < point[2]:
                    side[3] = True
            if point[1] - 5 < y_now + hayeler < point[3]:
                if point[0] < x_now < point[2] or point[0] < x_now + wlayer < point[2] or\
                   point[0] < x_now + wlayer // 2 < point[2] or point[0] < x_now + wlayer < point[2]:
                    side[2] = True
            if point[0] - 5 < x_now + wlayer < point[2] + 5:
                if point[1] < y_now < point[3] or point[1] < y_now + hayeler < point[3] or\
                   point[1] < y_now + hayeler // 2 < point[3] or point[1] < y_now + hayeler < point[3]:
                    side[1] = True
        return side
    else:
        print('non')


class Wall:
    def __init__(self, start, end, color_r):
        self.x_start = start[0]
        self.y_start = start[1]
        self.width = end[0] - self.x_start
        self.height = end[1] - self.y_start
        self.clr = py.color.Color(color_r)

    def draw(self):
        if (self.x_start, self.y_start, self.x_start + self.width, self.y_start + self.height) in walls_point:

            py.draw.rect(screen, self.clr, (self.x_start, self.y_start, self.width, self.height))
        else:
            walls_point.append((self.x_start, self.y_start, self.x_start + self.width, self.y_start + self.height))


class Sound:
    def __init__(self, start, end):
        self.x_start = start[0]
        self.y_start = start[1]
        self.width = end[0] - self.x_start
        self.height = end[1] - self.y_start
        self.clr = (255, 0, 0)
        self.center = (start[0] + end[0] // 2, start[1] + end[1] // 2)
        self.distance = 2
        self.line = xsc // 2
        self.volume = 0.0

    def listen(self, move_flag=False, base=(0, 0)):
        global x, y
        self.x_start, self.y_start = base[0], base[1] if move_flag else 0
        self.volume = 1 - self.distance / self.line if self.distance <= self.line else 0
        py.mixer.music.set_volume(self.volume)
        self.center = (self.x_start, self.y_start)
        self.distance = int(((self.center[0] - x) ** 2 + (self.center[1] - y) ** 2) ** 0.5)
        py.draw.rect(screen, self.clr, (self.x_start, self.y_start, self.width, self.height), 0)


def import_somefile():
    global walls_array
    for line in file:
        sp = line.rsplit('\n')[0].split(' ')
        print((int(eval(sp[0])), int(eval(sp[1]))), (int(eval(sp[2])), int(eval(sp[3]))))
        walls_array.append(Wall((int(eval(sp[0])), int(eval(sp[1]))), (int(eval(sp[2])), int(eval(sp[3]))), sp[4]))


ghost_yarik = Mob(x_ghost, y_ghost, 1, 'monster', 'image/pack 1/rl_ran.png', 'image/pack 1/rl_sty.png',
                  'image/pack 1/rl_sty.png')
yarik_voice = Sound((x // 2, y // 2), (x // 2 + 30, y // 2 + 30))
box_for_hide_1 = Hidden_box((xsc // 4, ysc // 4))
radio_box = Sound((x // 2, y // 2), (x // 2 + 30, y // 2 + 30))
py.mouse.set_visible(True)
pygame.mixer.music.load("sounds/choice.mp3")
pause = Pause()
# clock = py.time.Clock()
while True:
    stsc = True
    while stsc:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        start_screen()
        pygame.display.update()
    
    py.mouse.set_visible(False)
    screen.fill((0, 0, 0))
    pygame.display.update()
    py.mixer.music.load('sounds/grohot.mp3')
    py.mixer.music.play(-1)
    py.time.delay(5000)
    py.mixer.music.load('sounds/kaplya.mp3')
    py.mixer.music.play(-1)
    speed = 3
    tick = 0
    py.mixer.music.load('sounds/shum.mp3')
    py.mixer.music.play(-1)
    import_somefile()
    while True:
        user_visible = True
        tick += 1
        screen.fill((125, 125, 125))
        if tick % 10 >= 5:
            user = up
        else:
            user = down
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and\
                not keys[pygame.K_DOWN] and not keys[pygame.K_s] and not keys[pygame.K_d] and\
                not keys[pygame.K_w] and not keys[pygame.K_a]:
            user = state
        else:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 10 and \
                    not points_check(x, y, walls_point)[0]:
                x -= speed
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < xsc - 10 - wlayer and \
                    not points_check(x, y, walls_point)[1]:
                x += speed
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and y > 10 and not points_check(x, y, walls_point)[3]:
                y -= speed
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < ysc - 10 - hayeler and \
                    not points_check(x, y, walls_point)[2]:
                y += speed
        if keys[pygame.K_ESCAPE]:
            break
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = 10
            chastota_bienie = 2
        elif keys[pygame.K_p]:
            speed = 35
            chastota_bienie = 0
        elif keys[pygame.K_SPACE]:
            pause.open(keys)
        elif keys[ord('`')]:
            debugPoint += 1
            py.time.delay(400)
        else:
            speed = 3

        ghost_yarik.live('monster')
        box_for_hide_1.draw()
        if user_visible:
            screen.blit(user, (x, y))
        [wall.draw() for wall in walls_array]
        radio_box.listen()
        # screen.blit(fogs, (-x, -y))
        # screen.blit(darkness, (-xsc + x + 20, -ysc + y + 43))
        if debugPoint % 2 == 0:
            debugInfo(str(x) + str(y) + str(points_check(x, y, walls_point)))
        pygame.display.update()
        clock.tick(30)
