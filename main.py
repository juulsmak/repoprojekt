import pygame as pg

#start pygame
pg.init()
clock = pg.time.Clock()
fps = 60
screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))

#setup okna
pg.display.set_caption('isaac')
icon = pg.image.load('hiclipart.com.png')
pg.display.set_icon(icon)


bulletP_img = pg.image.load('bullet.png')
tilesz = 50



class Player():

    def __init__(self, x, y,speed = 1.75, range = 150,shotspeed = 3, slimespeed = 20):
        self.img = pg.image.load('slime.png')
        self.rect = self.img.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.shoot_cooldown = 0
        self.slimespeed = slimespeed
        self.range = range
        self.shotspeed = shotspeed


    def shoot(self, dir):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = self.slimespeed
            bulletP = Bullet(self.rect.centerx, self.rect.centery, dir, self.shotspeed, self.range)
            bulletP.add(bulletP_group)

    def update(self):
        dx = 0
        dy = 0

        #controls
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            dy -= self.speed
        if key[pg.K_s]:
            dy += self.speed
        if key[pg.K_d]:
            dx += self.speed
        if key[pg.K_a]:
            dx -= self.speed
        if key[pg.K_UP]:
            self.shoot('up')
        if key[pg.K_DOWN]:
            self.shoot('dwn')
        if key[pg.K_RIGHT]:
            self.shoot('rght')
        if key[pg.K_LEFT]:
            self.shoot('lft')
        #shooting
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -=1


    #collisions
        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.img, self.rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect, 2)



class Pokoj():
    def __init__(self, dane):
        kamienob = pg.image.load('kamien.png')
        self.tilelist = []

        rows = 0
        for row in dane:
            cols = 0
            for tile in row:
                if tile == 1:

                    kamien_rect = kamienob.get_rect()
                    kamien_rect.x = cols * tilesz
                    kamien_rect.y = rows * tilesz
                    tile = (kamienob,kamien_rect)
                    self.tilelist.append(tile)
                cols +=1
            rows +=1

    def draw(self):
        for tile in self.tilelist:
            screen.blit(tile[0], tile[1])
            pg.draw.rect(screen, (0,0,0), tile[1], 2)


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, dir, speed =3 , range = 150):
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.range = range
        self.image = bulletP_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.dir = dir

    def update(self):
        if self.range <= 0:
            self.kill()
        else:
            if self.dir == 'up':
                self.rect.y -= self.speed
            if self.dir == 'dwn':
                self.rect.y += self.speed
            if self.dir == 'rght':
                self.rect.x += self.speed
            if self.dir == 'lft':
                self.rect.x -= self.speed
            self.range -= self.speed


#grupa pocisków
bulletP_group = pg.sprite.Group()
bulletE_group = pg.sprite.Group()

pokojdane = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pokoj = Pokoj(pokojdane)
player = Player(300,300)


#game loop
gamerun = True
while gamerun == True:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamerun = False

    screen.fill((100,0,100))
    pokoj.draw()
    player.update()
    bulletP_group.update()
    bulletP_group.draw(screen)
    bulletE_group.update()
    bulletE_group.draw(screen)
    pg.display.update()