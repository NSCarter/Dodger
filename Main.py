import pygame

pygame.init()

size = (1000, 650)

white = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Dodger')

done = False

clock = pygame.time.Clock()

screen.fill(white)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()
    clock.tick(60)
pygame.quit()
