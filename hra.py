import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300, 250, 50, 50)

run = True
while run:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 1
    if keys[pygame.K_RIGHT]:
        player.x += 1
    if keys[pygame.K_UP]:
        player.y -= 1
    if keys[pygame.K_DOWN]:
        player.y += 1
    
    pygame.draw.rect(screen, (255, 128, 0), player)
    pygame.display.update()

pygame.quit()