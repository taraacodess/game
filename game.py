import pygame
pygame.init()

screen_width= 500
screen_height= 500

running= True

screen = pygame.display.set_mode((screen_width,screen_height))

#player variables
player_x=200
player_y=200
red=(255,0,0)
  
def draw():
    screen.fill(red)
    pygame.draw.rect(screen,(0,0,0),(player_x,player_y,20,20))
    pygame.display.update()

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    draw() 

pygame.quit()
print("helloworld")

