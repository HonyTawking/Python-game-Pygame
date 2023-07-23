import pygame
hp = 20
def get_damaged(hp, x):
    hp -= x
    return hp
def movement(x,y, direction):

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]) or (keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]) or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]) or (keys[pygame.K_UP] and keys[pygame.K_LEFT]):
        step=4
    else:
        step=5
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_LEFT]:
        x -= step
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        x += step
        direction = "RIGHT"
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step

    if (keys[pygame.K_s] and keys[pygame.K_a]) or (keys[pygame.K_s] and keys[pygame.K_d]) or (keys[pygame.K_w] and keys[pygame.K_d]) or (keys[pygame.K_w] and keys[pygame.K_a]):
        step=4
    else:
        step=5
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_a]:
        x -= step
        direction = "LEFT"
    if keys[pygame.K_d]:
        x += step
        direction = "RIGHT"
    if keys[pygame.K_w]:
        y -= step
    if keys[pygame.K_s]:
        y += step




    if x < 0:
        x = 0
    if x > 1160:
        x = 1160
    if y < 0:
        y = 0
    if y > 760:
        y = 760
    return x, y, direction