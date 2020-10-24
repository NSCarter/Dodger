import random

class Planet:
    def __init__(self, image, screenWidth):
        self.image = image # Choose randomly
        self.x = random.randint(0, screenWidth - 75) # 75 should be planet width
        self.y = 0 - 75
        self.speed = 4
        self.width = 75
        self.height = 75
        
    def draw(self, screen):
        self.y += self.speed
        screen.blit(self.image, (self.x, self.y))

    def getBoxX(self):
        return (self.x, self.x + self.width)

    def getBoxY(self):
        return (self.y, self.y + self.height)
