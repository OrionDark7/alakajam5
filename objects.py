import pygame

class counter(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/furniture/countertop.png")
        self.image = pygame.transform.scale(self.image, [120, 600])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])

class chair(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/furniture/seat.png")
        self.image = pygame.transform.scale(self.image, [75, 75])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)

class tools(pygame.sprite.Sprite):
    def __init__(self, pos, item):
        pygame.sprite.Sprite.__init__(self)
        if item == "stove":
            self.image = pygame.image.load("./images/furniture/stove.png")
            self.image = pygame.transform.scale(self.image, [120, 150])
        if item == "cutting board":
            self.image = pygame.image.load("./images/furniture/cutting-board.png")
            self.image = pygame.transform.scale(self.image, [60, 90])
        if item == "oven":
            self.image = pygame.image.load("./images/furniture/oven.png")
            self.image = pygame.transform.scale(self.image, [90, 120])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def click(self, mouse):
        clicked = False
        if self.rect.collidepoint(mouse):
            clicked = True
        return clicked
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])