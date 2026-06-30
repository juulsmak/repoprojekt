import pygame as pg
from rooms import Pokoj, pokojdane, screen
import random

#start pygame
pg.init()
clock = pg.time.Clock()
fps = 60



#setup okna
pg.display.set_caption('isaac')
icon = pg.image.load('hiclipart.com.png')
pg.display.set_icon(icon)

#images
enemy1_img = pg.image.load('enemy1.png')
bulletP_img = pg.image.load('bullet.png')





class Player(pg.sprite.Sprite):
    def __init__(self, x, y,health = 20,speed = 1.75, range = 150,shotspeed = 3, slimespeed = 20, dmg = 1):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('slime.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.health = health
        self.max_health = health

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.shoot_cooldown = 0
        self.slimespeed = slimespeed
        self.range = range
        self.shotspeed = shotspeed
        self.dmg = dmg


    def shoot(self, dir):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = self.slimespeed
            bulletP = Bullet(self.rect.centerx, self.rect.centery, dir, self.shotspeed, self.range)
            bulletP.add(bulletP_group)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

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
        #tiles
        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0



        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, speed = 1, dmg= 1, health = 100):
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = enemy1_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.cooldown = 40
        self.dmg = dmg
        self.health = health

    def update(self):
        dx = 0
        dy = 0
        if self.cooldown >0:
            self.cooldown -=1
        if self.cooldown == 0:
            #for x
            xcheck1 = abs(player.rect.centerx - (self.rect.centerx + self.speed) )
            xcheck2 = abs(player.rect.centerx - (self.rect.centerx - self.speed) )
            if self.rect.centerx == player.rect.centerx:
                dx = 0
            elif xcheck1 <= xcheck2:
                dx = self.speed
            else:
                dx = -self.speed

            #for y
            ycheck1 = abs(player.rect.centery - (self.rect.centery + self.speed))
            ycheck2 = abs(player.rect.centery - (self.rect.centery - self.speed) )
            if self.rect.centery == player.rect.centery:
                dy = 0
            elif ycheck1 <= ycheck2:
                dy = self.speed
            else:
                dy = -self.speed

    #collisions
        #tiles
        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0

        #player
        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
                player.health -= self.dmg
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0
                player.health -= self.dmg

        if self.health <0:
            self.kill()


        self.rect.x += dx
        self.rect.y += dy



class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, dir, speed =3 , range = 150, dmg = 1):
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.range = range
        self.dmg = dmg
        self.image = bulletP_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dir = dir

    def update(self):
        dx = 0
        dy = 0
        if self.range <= 0:
            self.kill()
        else:
            if self.dir == 'up':
                dy -= self.speed
            if self.dir == 'dwn':
                dy += self.speed
            if self.dir == 'rght':
                dx += self.speed
            if self.dir == 'lft':
                dx -= self.speed
            self.range -= self.speed

        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0
        if self in bulletP_group:
            for el in enemy_group:
                if pg.sprite.spritecollide(el, bulletP_group, False):
                    if el.alive():
                        el.health -= self.dmg
                        self.kill()
        else:
            if pg.sprite.spritecollide(player, bulletE_group, False):
                if player.alive():
                    player.health -= self.dmg
                    self.kill()


        self.rect.x += dx
        self.rect.y += dy


#grupa pocisków
bulletP_group = pg.sprite.Group()
bulletE_group = pg.sprite.Group()

enemy_group = pg.sprite.Group()


pokoj = Pokoj(pokojdane)
player = Player(300,300)
etest = Enemy(400, 400, 1, health = 5)
etest.add(enemy_group)


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
    enemy_group.update()
    enemy_group.draw(screen)

    pg.display.update()