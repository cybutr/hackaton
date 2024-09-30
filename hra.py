import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snake = [pygame.Rect(300, 250, 50, 50)]
direction = 'right'
score = 0

apple = pygame.Rect(random.randint(0, SCREEN_WIDTH - 50), random.randint(0, SCREEN_HEIGHT - 50), 20, 20)
apple_spawn_time = pygame.time.get_ticks()

run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    if keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    if keys[pygame.K_UP] and direction != 'down':
        direction = 'up'
    if keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'

    # Move snake
    head = snake[0]
    if direction == 'left':
        head.x -= 1
    if direction == 'right':
        head.x += 1
    if direction == 'up':
        head.y -= 1
    if direction == 'down':
        head.y += 1

    # Prevent snake from moving outside screen boundaries
    if head.x < 0:
        head.x = 0
    if head.x > SCREEN_WIDTH - head.width:
        head.x = SCREEN_WIDTH - head.width
    if head.y < 0:
        head.y = 0
    if head.y > SCREEN_HEIGHT - head.height:
        head.y = SCREEN_HEIGHT - head.height

    # Update snake body
    snake.insert(0, head)
    if len(snake) > score + 1:
        snake.pop()

    # Spawn apple every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - apple_spawn_time >= 5000:
        apple.x = random.randint(0, SCREEN_WIDTH - apple.width)
        apple.y = random.randint(0, SCREEN_HEIGHT - apple.height)
        apple_spawn_time = current_time

    # Check for collision with apple
    if snake[0].colliderect(apple):
        score += 1
        apple.x = random.randint(0, SCREEN_WIDTH - apple.width)
        apple.y = random.randint(0, SCREEN_HEIGHT - apple.height)

    # Check for collision with snake body
    for part in snake[1:]:
        if snake[0].colliderect(part):
            run = False

    # Draw snake and apple
    for part in snake:
        pygame.draw.rect(screen, (255, 128, 0), part)
    pygame.draw.rect(screen, (255, 0, 0), apple)
    pygame.display.update()

pygame.quit()