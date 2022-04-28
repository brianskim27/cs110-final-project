import pygame
import random

class Target(pygame.sprite.Sprite): 
   def __init__(self, width, height, diff_x, diff_y):
      """
      Creates a target for the user to click on to score a point
      args: self, width (int), height (int), diff_x (int), diff_y (int)
      return: none
      """
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('assets/target.png').convert_alpha()
      self.image = pygame.transform.scale(self.image, (diff_x + 10, diff_y + 10))
      self.rect = self.image.get_rect()
      self.rect.x = random.randrange(50, width-50) 
      self.rect.y = random.randrange(50, height-50) 
      self.width = width
      self.height = height
