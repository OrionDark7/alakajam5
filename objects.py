import pygame

class counter(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([120, 600])
        self.image.fill([206, 100, 2])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])

class chair(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([75, 75])
        self.image.fill([200, 200, 200])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)

class tools(pygame.sprite.Sprite):
    def __init__(self, pos, item):
        pygame.sprite.Sprite.__init__(self)
        if item == "stove":
            self.image = pygame.surface.Surface([120, 150])
            self.image.fill([128, 128, 128])
        if item == "cutting board":
            self.image = pygame.image.load("./images/cutting-board.png")
            self.image = pygame.transform.scale(self.image, [60, 90])
        if item == "oven":
            self.image = pygame.surface.Surface([80, 120])
            self.image.fill([128, 128, 128])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def click(self, mouse):
        clicked = False
        if self.rect.collidepoint(mouse):
            clicked = True
        return clicked
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])