def hitbox(fx,fy,ox,oy,W1X,W1Y,W2X,W2Y):
    hit = False
    for i in {fx, fx + W1X}:
        for j in {fy, fy + W1Y}:
            if ox <= i <= ox + W2X and oy <= j <= oy + W2Y:
                hit = True
    return hit

def circle_hitbox(wizx, wizy, r, oppx, oppy, woppx, woppy):
    hit = False
    Lista = [[oppx,oppy],[oppx+woppx//2,oppy],[oppx+woppx,oppy],[oppx,oppy+woppy//2],[oppx+woppx,oppy+woppy//2],[oppx,oppy+woppy],[oppx+woppx//2,oppy+woppy],[oppx+woppx,oppy+woppy]]
    for i in Lista:
        x2 = i[0]
        y2 = i[1]
        d = ((x2-wizx)*(x2-wizx)+(y2-wizy)*(y2-wizy))**(0.5)
        if d <= r:
            hit = True
    return hit