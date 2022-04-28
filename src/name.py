import pygame

class Name():
    def __init__(self, screen, color, name, x, y, width, height):
        """
        Creates a textbox for the user to click on and input a player name
        args: self, screen (surf), color (str), name (str), x (int), y (int), width (int), height (int)
        """
        self.x = x
        self. y = y

        self.width = width
        self.height = height
        
        self.font_name = pygame.font.Font('assets/blackhansans.ttf', 13)

        self.text_rect = pygame.Rect(self.x, self.y, self.width, self.height)
                
        pygame.draw.rect(screen, color, self.text_rect)

        text_name = self.font_name.render(str(name), True, (204, 0, 0))

        center_name = text_name.get_rect(center = (self.text_rect.x + width / 2, self.text_rect.y + height / 2))
                
        screen.blit(text_name, center_name)

    def is_pressed(self, pos, pressed):
        """
        Returns whether the textbox was clicked on
        args: self, pos (tuple), pressed (boolean)
        return: True if the textbox was clicked on, False if the mouse cursor is on the textbox
        """
        if self.text_rect.collidepoint(pos):
            if pressed[0]:
                return True
         
            return False