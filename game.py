import pygame
import opponent
import Wizard
import spells
import time
import hitbox
import bar

st = time.time()
pygame.init()
win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("RPG")

class image:
    tlo = pygame.image.load('tlo.png')
    wizard_R = pygame.image.load('wizard_right.png')
    wizard_L = pygame.image.load('wizard_left.png')
    death_L = pygame.image.load('death_left.png')
    death_R = pygame.image.load('death_right.png')
    fireball_right = pygame.image.load('fireball_rigt.png')
    fireball_left = pygame.image.load('fireball_left.png')
    fireball_icon = pygame.image.load('fireball_icon.png')
    fireball_animation1 = pygame.image.load('fireball_animation1.png')
    fireball_animation2 = pygame.image.load('fireball_animation2.png')
    fireball_animation3 = pygame.image.load('fireball_animation3.png')
    bar_gr = pygame.image.load('bar.png')


class winsize:
    w = 1200
    h = 800


class get_spell_animation:
    def __init__(self, x1, y1, size, start):
        self.x1 = x1
        self.y1 = y1
        self.size = size
        self.start = start


Bar3 = get_spell_animation(602, 401, 50, False)



szer = 40
wys = 40
x = winsize.w // 2
y = winsize.h // 2
opponentNumber_constant = 10
opponentNumber = opponentNumber_constant
step = 5
direction = "RIGHT"
opponents = opponent.opponent_list(opponentNumber, step)
cooldown_dmg = 0
ending = False
death_direction = image.death_R
circle = False
circle_cycles = 0
fireballs = [0, 0, 0]
fireballs_animation = [0, 0, 0]
fireball_speed = 10
fireball_dist = 420
cyklF = 0

while True:

    pygame.time.delay(20)
    cyklF += 1
    win.blit(image.tlo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # ------------------------------ movement

    x, y, direction = Wizard.movement(x, y, direction)

    if direction == "LEFT":
        win.blit(image.wizard_L, (x, y))
    else:
        win.blit(image.wizard_R, (x, y))

    # ------------------------------ hitboxes
    # ----------- Walking into opponent
    for i in range(opponentNumber):
        if hitbox.hitbox(x, y, opponents[i][0], opponents[i][1], 40, 40, 40, 40) == True and cooldown_dmg >= 0:
            Wizard.hp = Wizard.get_damaged(Wizard.hp, 20)
            opponents[i][2] = opponent.change_direct(opponents[i][2])
            if Wizard.hp <= 0:
                ending = True
            cooldown_dmg = -300
            print(Wizard.hp)
        cooldown_dmg += 1

    if cooldown_dmg > 1:
        cooldown_dmg = 1

    # ---------- Fireball into opponent
    for j in range(3):
        i = 0
        while i < opponentNumber:

            if fireballs[j] != 0 and fireballs[j] != 1:
                if hitbox.hitbox(fireballs[j][0], fireballs[j][1], opponents[i][0], opponents[i][1], 40, 24, 40,
                                 40) == True:
                    fireballs_animation[j] = [opponents[i][0], opponents[i][1], 18]
                    opponents.pop(i)
                    opponentNumber -= 1
                    i -= 1
                    fireballs[j] = 1

            i += 1
    # ------- Fireball animation
    for j in range(3):
        if fireballs_animation[j] != 0:
            if 12 < fireballs_animation[j][2] <= 18:    win.blit(image.fireball_animation1,
                                                                 (fireballs_animation[j][0], fireballs_animation[j][1]))
            if 6 < fireballs_animation[j][2] <= 12:     win.blit(image.fireball_animation2,
                                                                 (fireballs_animation[j][0], fireballs_animation[j][1]))
            if 0 < fireballs_animation[j][2] <= 6:      win.blit(image.fireball_animation3,
                                                                 (fireballs_animation[j][0], fireballs_animation[j][1]))
            fireballs_animation[j][2] -= 1
            if fireballs_animation[j][2] <= 0:
                fireballs_animation[j] = 0
    # ------------------------------- opponents movement
    for i in range(opponentNumber):
        opponents[i] = opponent.movement(opponents[i], step)
        k = 0  # auxiliary variable for opponents movement
        if opponents[i][4] == "LEFT": k = image.death_L
        if opponents[i][4] == "RIGHT": k = image.death_R

        win.blit(k, (opponents[i][0], opponents[i][1]))

    # ------------------------------- Fireball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        if fireballs[0] == 0 and cyklF > 0:
            fireballs[0] = spells.F1(x, y, direction, fireball_speed, fireball_dist)
            cyklF = 0
        elif fireballs[1] == 0 and cyklF > 8:
            fireballs[1] = spells.F1(x, y, direction, fireball_speed, fireball_dist)
            cyklF = 0
        elif fireballs[2] == 0 and cyklF > 8:
            fireballs[2] = spells.F1(x, y, direction, fireball_speed, fireball_dist)
            cyklF = 0
    if fireballs[0] == 1 and fireballs[1] == 1 and fireballs[2] == 1:
        cyklF = -36
        for i in range(3):
            fireballs[i] = 0

    # ------- Fireball movement
    for i in range(3):
        if fireballs[i] != 0 and fireballs[i] != 1:

            if fireballs[i][2] == "RIGHT":
                win.blit(image.fireball_right, (fireballs[i][0], fireballs[i][1]))
            else:
                win.blit(image.fireball_left, (fireballs[i][0], fireballs[i][1]))
            fireballs[i] = spells.fireball(fireballs[i])
            if len(fireballs[i]) == 0:
                fireballs[i] = 1
    # ----------------------------- Shield

    if keys[pygame.K_2] and circle_cycles >= 0:
        circle = True
        circle_cycles = 0
    if circle == True and circle_cycles <= 60 and circle_cycles >= 0:
        pygame.draw.circle(win, (30, 253, 240), (x + 20, y + 20), 41, 3)
        i = 0
        while i < opponentNumber:
            if hitbox.circle_hitbox(x + 20, y + 20, 41, opponents[i][0], opponents[i][1], 40, 40) == True:
                opponents.pop(i)
                opponentNumber -= 1
                i -= 1
            i += 1
    if circle_cycles > 60 and circle == True:
        circle_cycles -= 500
        circle = False
    circle_cycles += 1
    if circle_cycles > 100:
        circle_cycles = 100
    # ----------------------------- Spell cooldown animation
    if keys[pygame.K_3]:
        Bar3.start = True
    if Bar3.start == True:
        pygame.draw.circle(win, (100, 100, 100), (Bar3.x1, Bar3.y1), Bar3.size, 0)
        Bar3.size -= 0.4
        Bar3.x1 -= 1.8
        Bar3.y1 += 10
        if Bar3.y1 >= 777:
            Bar3.x1 = 534
            Bar3.y1 = 777
            Bar3.size = 20
            Bar3.start = False
    # -------------------------------- Bar
    win.blit(image.bar_gr, (419, 752))
    # ---- hp
    if Wizard.hp >= 50:
        pygame.draw.rect(win, (2.55 * (150 - Wizard.hp), 255, 0), (419, 740, 0.01 * Wizard.hp * 363, 4))
    elif Wizard.hp < 50:
        pygame.draw.rect(win, (255, 2.55 * Wizard.hp, 0), (419, 740, 0.01 * Wizard.hp * 363, 4))
    # ---- Fireball
    if cyklF < 0:
        pygame.draw.rect(win, (22, 117, 31), (bar.bar(0) + 2, 758, 36 + cyklF, 3))
    else:
        if fireballs.count(0) == 3:
            # caly zielony
            pygame.draw.rect(win, (22, 117, 31), (425, 758, 36, 3))
        elif fireballs.count(0) == 2:
            # 2/3 zolty
            pygame.draw.rect(win, (255, 255, 0), (425, 758, 24, 3))
        elif fireballs.count(0) == 1:
            # 1/3 czerwony
            pygame.draw.rect(win, (185, 20, 20), (425, 758, 12, 3))

    win.blit(image.fireball_icon, (bar.bar(0), 757))
    # ----Shield
    if 0 < circle_cycles <= 60 and circle == True:
        pygame.draw.rect(win, (22, 102, 255), (bar.bar(1) + 1, 758, 36 - circle_cycles * 0.6, 3))
    elif circle_cycles < 0:
        pygame.draw.rect(win, (22, 117, 31), (bar.bar(1) + 1, 758, 36 + circle_cycles * 0.072, 3))
    elif circle == False:
        pygame.draw.rect(win, (22, 117, 31), (bar.bar(1) + 1, 758, 36, 3))
    pygame.display.update()

    # ------------------------------- ending
    if ending == True:
        en = time.time()
        while True:
            czas = round(en - st, 2)
            pygame.time.delay(20)
            win.blit(image.tlo, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            text = 'your result is: ' + str(czas) + ' s'
            text_2 = 'Press space to play again <3'
            font = pygame.font.SysFont('comicsans', 30)
            label = font.render(text, 1, (255, 255, 255))
            label_2 = font.render(text_2, 1, (255, 255, 255))
            win.blit(label, (450, 350))
            win.blit(label_2, (400, 450))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                exit()

            if keys[pygame.K_SPACE]:
                ending = False
                czas = 0
                Wizard.hp = 100
                opponentNumber = opponentNumber_constant
                circle_cycles = 0
                st = time.time()
                x = winsize.w // 2
                y = winsize.h // 2
                opponents.clear()
                opponents = opponent.opponent_list(opponentNumber, step)
                for i in range(3):
                    fireballs[i] = 0

                break
            pygame.display.update()