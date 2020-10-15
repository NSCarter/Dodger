class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.changeX = 0
        self.changeY = 0
        self.width = 40

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
