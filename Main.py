# Put player into class
# Improve stuttering

import pygame

pygame.init()

size = (1000, 650)

white = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Dodger')

done = False

clock = pygame.time.Clock()

# <a href="https://www.freevector.com/space-rocket-vector--26316">FreeVector.com</a>
playerImage = pygame.image.load('rocket.JPG')
playerX = 480
playerY = 582
playerChangeX = 0
playerChangeY = 0

def drawPlayer(x, y):
    screen.blit(playerImage, (x, y))
    
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX -= 5
            if event.key == pygame.K_RIGHT:
                playerChangeX += 5
            if event.key == pygame.K_UP:
                playerChangeY -= 5
            if event.key == pygame.K_DOWN:
                playerChangeY += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerChangeY = 0

    playerX += playerChangeX
    playerY += playerChangeY

    screen.fill(white)

    drawPlayer(playerX, playerY)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
