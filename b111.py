import pyxel
import math
import random
pyxel.init(200, 200)
padx = 100
score = 0

class Ball:
    def __init__(self):
        self.x = random.randint(0,199)
        self.y = 0
        angle = math.radians(random.randint(30,150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
        self.direction = 1

def update():
    global padx, score
    i = 0
    for b in balls:
        b.x += b.vx * b.direction * 4
        b.y += b.vy * 4
        if b.y >= 200:
            if b.x >= 200 or b.x <= padx + 20:
                score += 1
            balls[i] = Ball()
        if b.x >= 200 or b.x <= 0:
            b.direction = b.direction * (-1)
        i += 1
    padx = pyxel.mouse_x

def draw():
    global padx, score
    pyxel.cls(7)
    for b in balls:
        pyxel.circ(b.x, b.y, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(5, 5, ('score:'+str(score)), 0)

balls = [Ball(), Ball(), Ball()]

pyxel.run(update, draw)