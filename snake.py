# configuração e importação de módulos
import pygame
from pygame.locals import *
from sys import exit
pygame.init()

# configuração da tela
L = 1024
A = 768
scr = pygame.display.set_mode((L, A))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Posição do jogador
X = L/2
Y = A/2

# loop
while True:
    clock.tick(60)
    scr.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                X = X - 10
            if event.key == K_RIGHT:
                X = X + 10
            if event.key == K_UP:
                Y = Y - 10
            if event.key == K_DOWN:
                Y = Y + 10'''

    if pygame.key.get_pressed()[K_LEFT]:
        X = X - 10
    if pygame.key.get_pressed()[K_RIGHT]:
        X = X + 10
    if pygame.key.get_pressed()[K_UP]:
        Y = Y - 10
    if pygame.key.get_pressed()[K_DOWN]:
        Y = Y + 10

    # desenhando player
    pygame.draw.rect(scr, (255, 0, 0), (X, Y, 20, 20))
    pygame.display.update()
