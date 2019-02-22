import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.right])