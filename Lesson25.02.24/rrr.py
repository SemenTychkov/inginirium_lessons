import pygame
import random

w,h =500,500

pygame.init()
win = pygame.display.set_mode((w,h))

object_to_draw=''

win.fill((255, 255, 255))
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()



    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        object_to_draw = 'квадрат'
    if keys[pygame.K_w]:
        object_to_draw = 'круг'
    if object_to_draw == 'круг':
        pygame.draw.circle(win, random.choices(range(256), k=3), (x, y), 30)
    if object_to_draw == 'квадрат':
        pygame.draw.rect(win, random.choices(range(256), k=3), (x, y, 50, 50))
    pygame.display.update()
    if keys[pygame.K_SPACE]:
        win.fill((255, 255, 255))



    pygame.time.delay(10)