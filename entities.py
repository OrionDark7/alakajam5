import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([50, 50])
        self.image.fill([122, 59, 1])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])

class customer(pygame.sprite.Sprite):
    def __init__(self, pos, order):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([50, 50])
        self.image.fill([255, 175, 102])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        self.order = str(order)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])
    def update(self, action, mouse, data):
        if action == "click" and self.rect.collidepoint(mouse):
            data["order"] = self.order
            data["pos"] = self.rect.left, self.rect.top
