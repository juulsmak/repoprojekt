import pygame as pg
from rooms import Map
from dane import *
import random
from button import Button

#start pygame
pg.init()
clock = pg.time.Clock()
fps = 60

start_game = False
game_over = False
end_game = False
boss_apeared = False


#setup okna
pg.display.set_caption('isaac')
icon = pg.image.load('img/bullet.png')
pg.display.set_icon(icon)
screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))


#images
heart1_img = pg.image.load('img/fullheart.png')
heart2_img = pg.image.load('img/emptyheart.png')
health_img = pg.image.load('img/heart.png')
range_img = pg.image.load('img/range.png')
dmg_img = pg.image.load('img/dmgup.png')
maxhealth_img = pg.image.load('img/maxhealth.png')
shotspeed_img = pg.image.load('img/shotspeed.png')
speed_img = pg.image.load('img/speed.png')
tears_img = pg.image.load('img/tears.png')
items_img = {
    'health': health_img,
    'range': range_img,
    'dmg': dmg_img,
    'maxhealth': maxhealth_img,
    'shotspeed': shotspeed_img,
    'speed': speed_img,
    'tears': tears_img
}
door_img = pg.image.load('img/door.png')
bulletP_img = pg.image.load('img/bullet.png')
kamienob = pg.image.load('img/rock.png')
menu_screen = pg.image.load('img/startscreen.png')
game_over_screen = pg.image.load('img/gameover.png')
you_won_screen = pg.image.load('img/youwin.png')
startbutton_img = pg.image.load('img/startbutton.png')
exitbutton_img = pg.image.load('img/exitbutton.png')
bg = pg.image.load('img/bg.png')



tilesz = 50
fade = pg.Surface((screen_size_x, screen_size_y), pg.SRCALPHA)
fadetime = 20

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, name,speed = 1, dmg= 1, health = 100):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.animation_list = []
        self.index = 0
        self.update_time = pg.time.get_ticks()
        self.action = 0

        animations = ['normal']

        for an in animations:
            temp_list = []
            for i in range(4):
                img = pg.image.load(f'img/{self.name}/{an}/{i}.png')
                temp_list.append(img)
            self.animation_list.append(temp_list)


        self.image = self.animation_list[self.action][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = speed
        self.cooldown = 40
        self.dmg = dmg
        self.health = health
    def update_animation(self):
        animation_cooldown = 200
        self.image = self.animation_list[self.action][self.index]
        if pg.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.index +=1
        if self.index >= len(self.animation_list[self.action]):
            self.index = 0




class Pokoj():
    def __init__(self):
        self.tilelist = []
        self.defeated = False
        self.doors = []
        self.changing = False
        self.boss_apeared = False

    def change(self,dane):
        self.defeated = False
        self.doors = []
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


                if tile == 4:
                    item = random.choice(list(items.keys()))
                    itemx = cols * tilesz
                    itemy = rows * tilesz
                    itemm = Item (itemx, itemy, item)
                    items_group.add(itemm)
                if tile == 3:
                    b = random.choice(bosses)
                    b.rect.x = cols * tilesz
                    b.rect.y = rows * tilesz
                    boss_group.add(b)
                    self.boss_apeared = True

                if tile == 2:
                    en = random.choice(enemies)
                    en.rect.x = cols * tilesz
                    en.rect.y = rows * tilesz
                    enemy_group.add(en)

                if tile == 5 or tile == 6 or tile == 7 or tile ==8:
                    door_rect = door_img.get_rect()
                    door_rect.x = cols * tilesz
                    door_rect.y = rows * tilesz
                    door = (tile, door_img,door_rect)
                    self.doors.append(door)

                cols +=1
            rows +=1

    def draw(self):
        for tile in self.tilelist:
            screen.blit(kamienob, tile[1])
        if self.defeated == True:
            for door in self.doors:
                screen.blit(pg.Surface((tilesz,tilesz)), door[2])
        else:
            for door in self.doors:
                screen.blit(door[1], door[2])

    def update(self):
        if not enemy_group:
            self.defeated = True
            enemy_group.empty()
            floor.mapdefeat[floor.current_ind] = True

    def change_room(self, dir):
        if dir == 5:
            floor.position[0] -= 1
            player.rect.x = int((screen_size_x + tilesz)/2)
            player.rect.y = screen_size_y - 2*tilesz
        if dir == 6:
            floor.position[1] += 1
            player.rect.x = tilesz
            player.rect.y = int((screen_size_y +tilesz)/2)
        if dir == 7:
            floor.position[0] += 1
            player.rect.x = int((screen_size_x + tilesz)/2)
            player.rect.y = tilesz
        if dir == 8:
            floor.position[1] -=1
            player.rect.x = screen_size_x - 2*tilesz
            player.rect.y = int((screen_size_y+tilesz)/2)

class Healthbar():
    def __init__(self):
        self.image1 = heart2_img
        self.image2 = heart1_img
        self.width = self.image1.get_width()
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.full = []
        self.empty = []

        for i in range(player.max_health):
            emp =  self.image2.get_rect()
            emp.x = 10 + self.width*i
            emp.y = 10
            self.empty.append(emp)

        for i in range(player.health):
            fll =  self.image1.get_rect()
            fll.x = 10 + self.width*i
            fll.y = 10
            self.full.append(fll)


    def draw(self):
        for el in self.empty:
            screen.blit(self.image1, el)

        for i in range(player.health):
            screen.blit(self.image2, self.full[i])


class Player(Entity):
    def __init__(self, x, y,name, health = 20,speed = 1.75, range = 150,shotspeed = 3, slimespeed = 20, dmg = 1):
        Entity.__init__(self, x, y, name, speed, dmg, health)

        self.max_health = health

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.shoot_cooldown = 0
        self.slimespeed = slimespeed
        self.range = range
        self.shotspeed = shotspeed
        self.dmg = dmg
        self.win = False


    def shoot(self, dir):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = self.slimespeed
            bulletP = Bullet(self.rect.centerx, self.rect.centery, dir, self.shotspeed, self.range, self.dmg)
            bulletP.add(bulletP_group)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def update(self):
        dx = 0
        dy = 0
        if self.alive():

            self.update_animation()

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
            #doors
            for door in pokoj.doors:
                if pokoj.defeated:
                    if pg.Rect.colliderect(self.rect, door[2]):
                        fade.fill((0,0,0))
                        items_group.empty()
                        pokoj.change_room(door[0])
                        new_map_index = floor.mapvar.index(floor.position)
                        pokoj.defeated = False
                        pokoj.change(floor.maprooms[new_map_index])
            self.rect.x += dx
            self.rect.y += dy


        if pokoj.boss_apeared == True and boss_group == False:
            self.win = True



        self.update_animation()
        screen.blit(self.image, self.rect)


class Enemy(Entity):
    def __init__(self, x, y, name, speed = 1, dmg= 1, health = 100, flying = False):
        Entity.__init__(self, x, y,name, speed , dmg, health)
        self.flying = flying

    def update(self):
        dx = 0
        dy = 0

        self.update_animation()

        if self.health <0:
            self.update_animation()
            self.kill()
            number = random.randint(1,10)
            if number > 7:
                item = random.choice(list(items.keys()))
                itemx = self.rect.centerx
                itemy = self.rect.centery
                itemm = Item(itemx, itemy, item)
                items_group.add(itemm)
            else:
                if number > 5:
                    itemx = self.rect.centerx
                    itemy = self.rect.centery
                    itemm = Item(itemx, itemy, 'health')
                    items_group.add(itemm)
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
        if self.flying == False:
            for tile in pokoj.tilelist:
                #for y
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    dy = 0
                #for x
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx= 0

        #player
        if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            dy = -3*dy
            if self.cooldown == 0:
                player.health -= self.dmg
                self.cooldown = 30
        if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            dx = -3*dx
            if self.cooldown == 0:
                player.health -= self.dmg
                self.cooldown = 30




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
            for el in boss_group:
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

class Item(pg.sprite.Sprite):
    def __init__(self, x, y, name):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.image = items_img[self.name]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        if pg.sprite.spritecollide(self, player_group, False):
            items[self.name][0] += items[self.name][1]
            print(player.health)
            self.kill()






floor = Map()

#buttons
start_button = Button(20, 400, startbutton_img)
exit_button = Button(520, 400, exitbutton_img)

#grupa pocisków
bulletP_group = pg.sprite.Group()
bulletE_group = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
items_group = pg.sprite.Group()
boss_group = pg.sprite.Group()



enemies = [
    Enemy(0,0,'walker',2,1,50),
    Enemy(0,0,'walker',1,2,100),
    Enemy(0,0,'walker',4,1,50),
    Enemy(0,0,'flyer',2,1,50, flying=True),
    Enemy(0,0,'flyer',1,2,100, flying = True),
    Enemy(0,0,'flyer',4,1,25, flying = True)
           ]
bosses = [
    Enemy(0,0,'boss',2,2,150),
    Enemy(0, 0, 'boss', 3, 2, 125, flying = True)
]
player = Player(500, 300, 'player', health = 10, dmg = 20, speed = 5)
player.add(player_group)
healthbar = Healthbar()

items = {
    'health': [player.health, 1],
    'range': [player.range, 50],
    'dmg': [player.dmg, 1],
    'maxhealth': [player.max_health, 1],
    'shotspeed': [player.shotspeed, 1],
    'speed': [player.speed, 1],
    'tears': [player.slimespeed, 2]
}
pokoj = Pokoj()
pokoj.change(floor.startingroom)

#game loop
gamerun = True
while gamerun == True:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamerun = False

    if start_game == False:
        screen.blit(menu_screen, menu_screen.get_rect())
        if start_button.draw(screen):
            start_game =True
        if exit_button.draw(screen):
            gamerun = False
    else:
        if player.alive() == False:
            screen.blit(game_over_screen, game_over_screen.get_rect())
            if exit_button.draw(screen):
                gamerun = False
        else:
            if player.win == True:
                screen.blit(you_won_screen, you_won_screen.get_rect())
                if exit_button.draw(screen):
                    gamerun = False
            else:
                screen.blit(bg, bg.get_rect())
                pokoj.draw()
                player.update()
                enemy_group.update()
                pokoj.update()
                bulletP_group.update()
                bulletP_group.draw(screen)
                enemy_group.update()
                enemy_group.draw(screen)
                boss_group.update()
                boss_group.draw(screen)
                items_group.update()
                items_group.draw(screen)
                healthbar.draw()

    pg.display.update()
