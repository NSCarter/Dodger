import pygame
import Player

pygame.init()

size = (1000, 650)

white = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Dodger')

done = False

clock = pygame.time.Clock()

# <a href="https://www.freevector.com/space-rocket-vector--26316">FreeVector.com</a>
player = Player.Player(pygame.image.load('rocket.JPG'), 480, 582)
    
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changeX -= 5
            if event.key == pygame.K_RIGHT:
                player.changeX += 5
            if event.key == pygame.K_UP:
                player.changeY -= 5
            if event.key == pygame.K_DOWN:
                player.changeY += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.changeY = 0

    player.x += player.changeX
    player.y += player.changeY

    screen.fill(white)

    player.draw(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
