import pygame

pygame.init()

width = 500
height = 500


win = pygame.display.set_mode((width, height))

xCircle = width / 2
yCircle = height / 2
x = width / 2
y = height / 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    # Если стрелка влево
    if keys[pygame.K_LEFT]:
        # то
        xCircle -= 5
    # Если стрелка вправо
    elif keys[pygame.K_RIGHT]:
        # то
        xCircle += 5
    # Если стрелка вверх
    elif keys[pygame.K_UP]:
        # то
        yCircle -= 5
    # Если стрелка вниз
    elif keys[pygame.K_DOWN]:
        # то
        yCircle += 5
    # Иначе
    else:
        xCircle = width / 2
        yCircle = height / 2
    if xCircle < x - 150:
        pygame.time.delay(100)

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 255, 0), (xCircle, yCircle), 30)
    pygame.display.update()
    pygame.time.delay(10)
