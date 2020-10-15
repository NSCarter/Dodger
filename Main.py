import pygame
import Player
import Planet

pygame.init()

size = (1000, 650)

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Dodger')

done = False

clock = pygame.time.Clock()

# <a href="https://www.freevector.com/space-rocket-vector--26316">FreeVector.com</a>
player = Player.Player(pygame.image.load('rocket.JPG'), 480, 582)
planet = Planet.Planet(pygame.image.load('planet.PNG'), size[0])
    
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
    planet.draw(screen)

    # Move to function
    if player.y < planet.y + planet.height:
        if player.x > planet.x and player.x < planet.x + planet.width or player.x + player.width > planet.x and player.x + player.width < planet.width:
           pygame.quit() # Make nice

    if(planet.y > 650): # Change to timed
        planet = Planet.Planet(pygame.image.load('planet.PNG'), size[0])

    pygame.display.update()
    clock.tick(60)
pygame.quit()
