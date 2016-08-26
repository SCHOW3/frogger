##TODO Make class

import pygame,os,sys, random

from pygame.locals import *

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super(Frog,self).__init__()
        self.frogimage = pygame.image.load("frog.jpg").convert()
        self.image = self.frogimage
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 200
        ##self.startpos = (self.rect.x,self.rect.y)
        self.image.set_colorkey((255,255,255))

    def move(self):
        self.rect.move(self.move(self.rect.x,self.rect.y))

    def up(self):
        self.rect.y -= 20

    def down(self):
        self.rect.y += 20

    def left(self): 
        self.rect.x -= 20

    def right(self):
        self.rect.x += 20

 
pygame.init()
screen_width = 700
screen_height = 400

screen = pygame.display.set_mode([screen_width,screen_height])
all_sprites_list = pygame.sprite.Group()
done = False
clock = pygame.time.Clock()
player = Frog()
all_sprites_list.add(player)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.up()
            if event.key == pygame.K_DOWN:
                player.down()
            if event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_RIGHT:
                player.right()
    screen.fill((255,255,255))
    all_sprites_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
