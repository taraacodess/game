import pygame
import random

pygame.init()

# Screen setup // Or setup to make the game window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# Game variables || Players and Food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
food_pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]

# Game loop
game_over = False
clock = pygame.time.Clock()

def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(segment[0], segment[1], 10, 10))

def draw_food():
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

def is_collision():
    # Check if snake collides with walls or itself
    if snake_pos in snake_body[1:] or not (0 <= snake_pos[0] < 400 and 0 <= snake_pos[1] < 400):
        return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Snake body growth and food consumption
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        print("Khayo")
        food_pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
    else:
        snake_body.pop()
    

    # Draw everything
    screen.fill((0, 0, 0))
    draw_snake()
    draw_food()

    if is_collision():
        game_over = True

    pygame.display.update()
    clock.tick(8)

pygame.quit()