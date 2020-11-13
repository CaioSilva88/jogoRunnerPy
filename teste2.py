import pygame
import os
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'  # sempre no centro da tela


pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Jogo Arcade Runner')
relogio = pygame.time.Clock()
azul = (55,158,199)
chao = pygame.image.load('chao.png')

p1 = pygame.image.load('p1.png')

    #p1 = range(5)


p2 = pygame.image.load('p01.png')
inimigo_red = pygame.image.load('RED.png')
inimigo_blue = pygame.image.load('BLUE.png')
x01 = 20
y01 = 140
x2 = 700
y2 = 200   #250
x3 = 300
y3 = 250   # em cima
b1 = pygame.Rect(100, 250, 10, 10)
o1 = pygame.Rect(x2,y2,10,10)
velocidade = 5
velocidade2 = 10

sair = True


#funcao para a animacao do personagem. Troca de frame
def get_frame_by_gid(gid):
    global p1
    colunas = 5

    if(gid ==0):

        largura = 153
    if(gid == 1):
        largura = 161
    if(gid == 2):
        largura = 163
    if(gid == 3):
        largura = 170


    altura = 200
    space_h = 0
    margin = 0
    top = 0
    space_v = 0
    linha = gid / colunas
    coluna = gid % colunas
    x = (coluna *(largura + space_h)) + margin
    y = (linha *(altura + space_v)) + top
    quadro = p1.subsurface(pygame.Rect((x,y), (largura,altura)))
    return quadro

quadro = 0



while sair:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                    x01 =20
                    y01 = 120

            if event.key == pygame.K_DOWN:
                    x01 = 20
                    y01 = 140
                #blits embaixo



        tela.fill((azul))
        x2-=velocidade

        x3 -= velocidade


        tela.blit(chao, [0, 300])



        if((x3 < 10 and x2 )):
            x3 = randint(610,1000)
        if(x2 < 10):
            x2 = randint(1500,1800)


        if(x3 < x01 + 140 and y01+210 == y3+100):
            y01 = - 200
        if(x01 + 140 > x2 and y01+200 == y2+120):
            y01 = - 200





        tela.blit(inimigo_blue,[x2,y2])



        frame = get_frame_by_gid(quadro)
        quadro += 1
        if quadro >= 4:
            quadro = 0
        tela.blit(frame, (x01, y01))

        tela.blit(inimigo_red, [x3, y3])



        relogio.tick(15)
        pygame.display.update()


pygame.quit()
