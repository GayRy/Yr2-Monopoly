import pygame

class Piece:
    def __init__(self,image,all_attributes, screen):
        self.image = image
        self.all_attributes = all_attributes
        self.screen = screen

    def Place_Option(self,window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.image_width, self.image_height), 8)
        image = pygame.transform.scale(self.image,(self.image_width, self.image_height))
        self.screen.blit(image,(self.x, self.y))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.image_width:
            if pos[1] > self.y and pos[1] < self.y + self.image_height:
                return True
        return False
