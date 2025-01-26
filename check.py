import pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500

# Initialize the game
running = True
screen = pygame.display.set_mode((screen_width, screen_height))

# Player variables
player_x = 200
player_y = 200
red = (2, 48, 32)
player_speed = 5

def draw():
    # Clear the screen and draw the player
    screen.fill(red)
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, 20, 20))
    pygame.display.update()

def is_collision():
    # Check if the player touches any wall
    if player_x <= 0 or player_x >= screen_width - 20 or player_y <= 0 or player_y >= screen_height - 20:
        pygame.quit()  # Close the game window
        print("Game Over!")  # Print a game-over message
        exit()  # Exit the program

while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Collision check
    is_collision()

    # Redraw the screen
    draw()

pygame.quit()
