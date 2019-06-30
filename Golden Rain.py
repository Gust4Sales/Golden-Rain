import pygame as pg
from random import randint


width = 900
height = 620
cor = (138, 43, 226)
# cor = (255, 215, 0) // golden 
background = (230, 230, 250)


class Rain(object):
    def __init__(self):
        self.x = randint(0, width)
        self.y = randint(-400, -200)
        self.speed = randint(2, 20)
        self.size = randint(10, 25)

    def fall(self):
        self.y += self.speed
        # self.speed += 0.05 Gravidade
        if self.y > height:
            self.ellipse()
            self.y = randint(-400, -200)
            self.speed = randint(2, 20)

    def show(self):
        pg.draw.line(win, cor, [self.x, self.y], [self.x, self.y + self.size], 1)

    def ellipse(self):
        pg.draw.ellipse(win, cor, (self.x - 10, self.y - 10, 20, 10))


def main():
    drops = []
    clock = pg.time.Clock()

    for _ in range(600):
        drop = Rain()
        drops.append(drop)

    while True:
        # Eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        win.fill(background)

        for c in range(len(drops)):
            drops[c].fall()
            drops[c].show()

        clock.tick(30)
        pg.display.update()


pg.display.init()
pg.display.set_caption('Purple Rain')
win = pg.display.set_mode([width, height])
pg.mixer.init()
pg.mixer.music.load('Chuva.mp3')
pg.mixer.music.play(-1)

main()
