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

score = 0
planetTimer = 4000

# <a href="https://www.freevector.com/space-rocket-vector--26316">FreeVector.com</a>
player = Player.Player(pygame.image.load('rocket.JPG'), 480, 582)
planets = [Planet.Planet(pygame.image.load('planet.PNG'), size[0])]

NEWPLANETEVENT = pygame.USEREVENT + 1

pygame.time.set_timer(NEWPLANETEVENT, planetTimer)

def isOverlapping1D(box1, box2):
    return box1[1] >= box2[0] and box2[1] >= box1[0]

def checkOverlap():
    for planet in planets:
        if (isOverlapping1D(player.getBoxX(), planet.getBoxX()) and isOverlapping1D(player.getBoxY(), planet.getBoxY())):
            return True
    return False

def displayScore():
    font = pygame.font.SysFont(None, 25)
    text = font.render('Score: ' + str(score), True, black)
    screen.blit(text, (0,0))
    
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
        if event.type == NEWPLANETEVENT:
            planets.append(Planet.Planet(pygame.image.load('planet.PNG'), size[0]))


    player.x += player.changeX
    player.y += player.changeY

    screen.fill(white)

    player.draw(screen)
    
    for planet in planets:
        planet.draw(screen)

    if (checkOverlap()):
        done = True

    for planet in planets:
        if planet.y > 650:
            planets.remove(planet)
            planetTimer -= 1
            score += 1

    displayScore()
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()
