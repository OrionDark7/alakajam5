import pygame

class button(pygame.sprite.Sprite):
    def __init__(self, text, pos):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 24)
        self.text = str(text)
        self.image = self.font.render(str(text), 1, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        self.clicked = False
    def click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.clicked = True
        return self.clicked
    def draw(self, surf):
        surf.blit(self.image, [self.rect.left, self.rect.top])
    def reset(self):
        self.clicked = False
    def color(self, color):
        self.image = self.font.render(self.text, 1, list(color))