import pygame

class Reticle(pygame.sprite.Sprite):
   def __init__(self): 
      """
      Creates a reticle that will follow the mouse on the screen
      args: self
      return: none
      """
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('assets/reticle.png').convert_alpha()
      self.image = pygame.transform.scale(self.image, (15, 15))
      self.rect = self.image.get_rect()
      self.rect.x = 250
      self.rect.y = 250
      
   def update(self,x, y):
      """
      Allows the reticle to move
      args: self, x (int), y (int)
      return: none
      """
      self.rect.x = x
      self.rect.y = y
