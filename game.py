import pygame
pygame.init()

screen_width= 500
screen_height= 500

running= True

screen = pygame.display.set_mode((screen_width,screen_height))

#player variables
player_x=200
player_y=200
red=(2, 48, 32)
player_speed=5


  
def draw():
    screen.fill(red)
    pygame.draw.rect(screen,(0,0,0),(player_x,player_y,20,20))
    
   

def is_collision():
    if player_x== 500:
        pygame.quit()

    elif player_y==500:
        pygame.quit()  



while running :
    
    pygame.time.delay(20)
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running= False
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x-= player_speed

    if keys [pygame.K_RIGHT]:
        player_x+=player_speed

    if keys[pygame.K_UP]:
        player_y-=player_speed

    if keys[pygame.K_DOWN]:
        player_y+=player_speed

    if player_x >= 485:
        player_x -= 5   

    if player_y >= 485:
        player_y -= 5    

    if player_y <= 0:
        player_y += 5

    if player_x <= 0:
        player_x += 5    

        
    draw()  
    is_collision()  
    pygame.display.update()
pygame.quit()
print("helloworld")

