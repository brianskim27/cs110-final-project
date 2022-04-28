import pygame
import random

class Snake(pygame.sprite.Sprite): 
    def __init__(self, width, height):
        """
        Creates a snake that a user can click on, which will result in a point deduction
        args: self, width (int), height (int)
        return: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/snake.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, width-50) 
        self.rect.y = random.randrange(50, height-50)
        self.width = width
        self.height = height
      
    def update(self):
        """
        Moves the snakes around in random locations
        args: self
        return: none
        """
        self.rect.x = random.randrange(50,  self.width-50)
        self.rect.y = random.randrange(50, self.height-50)