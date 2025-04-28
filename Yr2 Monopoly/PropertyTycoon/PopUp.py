import pygame

class PopUp():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.scale = scale

    def draw(self, surface, text):
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        message = font.render(text, True, (0, 0, 0))
        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(message, (self.rect.x, self.rect.y))