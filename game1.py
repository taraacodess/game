import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.Font(None, 35)  # Default font with size 35

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
food_pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
score = 0
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

def display_score():
    # Render the score text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 10))  # Draw text at the top-left corner

# Game loop
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

    # Update snake's position
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
        score += 1
        food_pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
    else:
        snake_body.pop()

    # Check for collisions
    if is_collision():
        game_over = True

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen with black
    draw_snake()
    draw_food()
    display_score()  # Display the current score

    pygame.display.update()
    clock.tick(10)

pygame.quit()
