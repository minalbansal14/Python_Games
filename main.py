import pygame
import random
pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Game specific Variables
exit_game = False
window_width=800
window_height=500
snake_x=50
snake_y=50
snake_size=5
food_x=random.randint(5,window_width)
food_y=random.randint(5,window_height)

#creating Window
gamewindow = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("My First Project")


#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right")


    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,(snake_x,snake_y,snake_size,snake_size))
    pygame.draw.rect(gamewindow,red,(food_x,food_y,snake_size,snake_size))
    pygame.display.update()
pygame.quit()
quit()
