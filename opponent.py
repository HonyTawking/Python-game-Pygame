import random


def losuj():
    binx = random.randint(0,1)
    biny = random.randint(0,1)
    if binx == 0:
        hx = random.randrange(520)
    else:
        hx = random.randrange(680,1160)
    if biny == 0:
        hy = random.randrange(320)
    else:
        hy = random.randrange(480,760)
    return hx, hy


def direct():
    direction = random.randrange(1,5,1)
    return direction

def dist(step):
    dist = random.randrange(15,80,1)
    dist *= step
    return dist

def opponent_list(opponentNumber, step):
    opponents = []
    for i in range(opponentNumber):
        A = []
        ox, oy = losuj()
        direction = direct()
        dystans = dist(step)
        A.append(ox)
        A.append(oy)
        A.append(direction)
        A.append(dystans)
        A.append("RIGHT")
        opponents.append(A)
    return opponents

def movement(opponents, step):

        #==== direction
        if opponents[2] == 1:
            opponents[1] -= step
        elif opponents[2] == 3:
            opponents[1] += step
        elif opponents[2] == 2:
            opponents[0] += step
        elif opponents[2] == 4:
            opponents[0] -= step


        opponents[3] -= step
        if opponents[3] <= 0:
            opponents[2] = direct()
            opponents[3] = dist(step)
        if opponents[1] <= 0:
            opponents[2] = 3
        if opponents[0] <= 0:
            opponents[2] = 2
        if opponents[1] >= 760:
            opponents[2] = 1
        if opponents[0] >= 1160:
            opponents[2] = 4
        if opponents[2] == 4: opponents[4] = "LEFT"
        if opponents[2] == 2: opponents[4] = "RIGHT"
        return opponents
def change_direct(direct):
    if direct == 1:
        direct = 3
    elif direct == 2:
        direct = 4
    elif direct == 3:
        direct = 1
    elif direct == 4:
        direct = 2
    return  direct