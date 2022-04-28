import pygame


class Button:
   def __init__(self, x, y, width, height, fg, bg, content, fontsize):
      """
      Creates a button that is used to navigate around the menus
      args: self, x (int), y (int), width (int), height (int), fg (RGB), bg (RGB), content (string), fontsize (int)
      return: none
      """
      self.font = pygame.font.Font('assets/blackhansans.ttf', fontsize)
      self.content = content

      self.x = x
      self.y = y

      self.width = width
      self.height = height

      self.fg = fg
      self.bg = bg

      self.image = pygame.Surface((self.width, self.height))
      self.image.fill(self.bg)
      self.rect = self.image.get_rect()

      self.rect.x = self.x
      self.rect.y = self.y

      self.text = self.font.render(self.content, True, self.fg)
      self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
      self.image.blit(self.text, self.text_rect)

   def is_pressed(self, pos, pressed):
      """
      Returns whether a button was clicked on
      args: self, pos (tuple), pressed (boolean)
      return: True if button was clicked on, False if the mouse cursor is on the button
      """
      if self.rect.collidepoint(pos):
         if pressed[0]:
            return True
         
         return False