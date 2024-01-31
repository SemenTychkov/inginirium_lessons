import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

xRectangle = 150
y = 150
i = 250
o =250
xKvadrat = 200
z = 200
x2 = 0
y2 = 500
tipa=1
tipaO=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    xRectangle = xRectangle + tipa
    o = o + tipaO
    xKvadrat = xKvadrat + tipa
    z = z + tipaO

    if o>500:
        tipaO = -1
    if o<0:
        tipaO = 1
    if xRectangle>500:
        tipa = -1
    if xRectangle<0:
       tipa=1
    if z>500:
        tipa = -1
    if z<0:
       tipa= 1

    win.fill((255,255,255))
    pygame.draw.rect(win,(255,255,0), (xRectangle,y,100,150))
    pygame.draw.circle(win, (0, 255, 255), (i, o), 50)
    pygame.draw.rect(win, (255, 0, 0), (xKvadrat, z, 50, 50))
    pygame.display.update()
    pygame.time.delay(10)



