def fireball(fireball):
    #[x, y, kierunek, fireball_speed, dist]
    if fireball[2] == "RIGHT":
        fireball[0] += fireball[3]
    else:
        fireball[0] -= fireball[3]
    fireball[4] -= fireball[3]
    if fireball[4] <= 0:
        fireball = []

    return fireball

def F1(x, y, direction, fireball_speed, fireball_dist):
    A = []
    if direction == "RIGHT":
        A.append(x + 40)
    else:
        A.append(x - 40)
    A.append(y + 8)
    A.append(direction)
    A.append(fireball_speed)
    A.append(fireball_dist)
    return A