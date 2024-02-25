import pygame
import random

GRAY = [70] *4
BLACK = [0] *4
WHINE = [255] *4
W,H =500,500

pygame.init()
win = pygame.display.set_mode((W,H))

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(10):
        pygame.draw.circle(win,GRAY,\
                           (random.randint(0,W), random.randint(0,H)),1)

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win,WHINE,pos,5)
    pygame.display.update()

    pygame.time.delay(10)