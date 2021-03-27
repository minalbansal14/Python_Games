import pygame
pygame.init()


#creating Window
gamewindow = pygame.display.set_mode((800,500))
pygame.display.set_caption("My First Project")

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Game specific Variables
exit_game = False


#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right")


    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,(50,50,5,5))
    pygame.display.update()
pygame.quit()
quit()
