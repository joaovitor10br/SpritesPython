import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

preto = ((0,0,0))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('Sprites/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        proporcional = 128*3, 64*3
        self.image = pygame.transform.scale(self.image, proporcional)

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def atacar(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = 0
            self.image = self.sprites[int(self.atual)]
            proporcional = 128*3, 64*3
            self.image = pygame.transform.scale(self.image, proporcional)

grupo_sprites = pygame.sprite.Group()
sapo = Sapo()
grupo_sprites.add(sapo)

relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    grupo_sprites.draw(tela)
    grupo_sprites.update()
    pygame.display.flip()
