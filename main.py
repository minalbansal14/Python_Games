import pygame
import random
pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Game specific Variables
exit_game = False
window_width = 800
window_height = 500
snake_x = 50
snake_y = 50
snake_size = 25
velocity_x = 0
velocity_y = 0
food_x = random.randint(50, window_width-50)
food_y = random.randint(50, window_height-50)
fps = 20
score =0
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

#creating Window
gamewindow = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My First Project")


#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = velocity_x + 10
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = velocity_x - 10
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = velocity_y - 10
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = velocity_y + 10
                velocity_x = 0

    snake_x = snake_x+velocity_x
    snake_y = snake_y+velocity_y
    if((abs(snake_x-food_x)<10) and (abs(snake_y-food_y)<10)):
        score = score+10
        food_x = random.randint(5, window_width)
        food_y = random.randint(5, window_height)

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,(snake_x,snake_y,snake_size,snake_size))
    pygame.draw.rect(gamewindow,red,(food_x,food_y,snake_size,snake_size))
    text = font.render(f'Score: {score}', True, red)
    gamewindow.blit(text,(5,5))
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
