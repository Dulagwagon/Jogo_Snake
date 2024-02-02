# configuração e importação de módulos
import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

# configuração de música e som
pygame.mixer.music.set_volume(0.25)
bgmusic = pygame.mixer.music.load('BoxCat Games - Storm.mp3')
pygame.mixer.music.play(-1)
colsnd = pygame.mixer.Sound('smw_jump.wav')
colsnd.set_volume(1.2)

# configuração da tela
L = 1024
A = 768
scr = pygame.display.set_mode((L, A))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
pts = 0
txt = pygame.font.SysFont("Gill Sans", 35)

# Posição do jogador e do ponto
X = int(L/2)
Y = int(A/2)
xdot = randint(20, 980)
ydot = randint(20, 740)

# loop
while True:
    clock.tick(60)
    scr.fill((0, 0, 0))
    msg = f'Pontos: {pts}'
    txtF = txt.render(msg, True, (255, 255, 255))
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
        X = X - 5
    if pygame.key.get_pressed()[K_RIGHT]:
        X = X + 5
    if pygame.key.get_pressed()[K_UP]:
        Y = Y - 5
    if pygame.key.get_pressed()[K_DOWN]:
        Y = Y + 5

    # desenhando player
    player = pygame.draw.rect(scr, (255, 0, 0), (X, Y, 20, 20))
    dot = pygame.draw.rect(scr, (0, 0, 255), (xdot, ydot, 20, 20))

    if player.colliderect(dot):
        xdot = randint(20, 980)
        ydot = randint(20, 740)
        pts = pts + 1
        colsnd.play()

    scr.blit(txtF, (20,20))
    pygame.display.update()
