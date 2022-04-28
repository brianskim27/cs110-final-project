import sys
import pygame
import random
import src.snake
import src.target
import src.reticle
import src.leaderboard
import src.button
import src. name


class Controller:
   def __init__(self, width=600, height=400):
      """
      Initializes the variables needed to control the program
      args: self, width=600 (int), height=400 (int)
      return: none
      """
      #Pygame.inits
      pygame.init()
      pygame.mixer.init()
      pygame.font.init()

      #Gunshot sound
      self.gunshot = pygame.mixer.Sound('assets/sound.wav')
      self.gunshot.set_volume(0.2)
      
      #Dimensions      
      self.width = width
      self.height = height

      self.target_width_easy = 50
      self.target_height_easy = 50

      self.target_width_hard = 35
      self.target_height_hard = 35

      self.target_width_pro = 20
      self.target_height_pro = 20
      
      #Display      
      self.screen = pygame.display.set_mode((self.width, self.height))
      self.screen.fill((0, 0, 0))

      self.game_background = pygame.image.load('assets/gamebackground.jpg').convert_alpha()
      self.game_background = pygame.transform.scale(self.game_background, (self.width, self.height))

      self.intro_background = pygame.image.load('assets/introbackground.jpeg').convert_alpha()
      self.intro_background = pygame.transform.scale(self.intro_background, (self.width, self.height))
      
      self.endscreen_background = pygame.image.load('assets/gameoverscreen.jpeg').convert_alpha()
      self.endscreen_background = pygame.transform.scale(self.endscreen_background, (self.width, self.height))
      
      self.rules_background = pygame.image.load('assets/rulesscreen.jpeg').convert_alpha()
      self.rules_background = pygame.transform.scale(self.rules_background, (self.width, self.height))
 
      self.difficulty_background = pygame.image.load('assets/difficulty.jpeg').convert_alpha()
      self.difficulty_background = pygame.transform.scale(self.difficulty_background, (self.width, self.height))

      self.leaderboard_background = pygame.image.load('assets/leaderboard.jpeg').convert_alpha()
      self.leaderboard_background = pygame.transform.scale(self.leaderboard_background, (self.width, self.height))
      
      pygame.display.set_caption("Aim Trainer")
      pygame.display.set_icon(pygame.image.load("assets/reticle.png"))

      #Clock/timer
      self.clock = pygame.time.Clock()
      self.timer = 60
      self.timer_string = "Time Remaining: {}".format(self.timer)
      pygame.time.set_timer(pygame.USEREVENT, 1000)

      #Scoring
      self.score = 0
      self.score_string = "Score: {}".format(self.score)

      self.accuracy = 100
      self.accuracy_string = "Accuracy: {}%".format(self.accuracy)

      self.clicks = 0
      
      #Reticle
      self.mouse_x = 0  
      self.mouse_y = 0

      self.mouse_pos = (pygame.mouse.get_pos())

      self.reticle = pygame.sprite.Group()
      self.reticle.add(src.reticle.Reticle())
      
      pygame.mouse.set_visible(True)
      
      #Target
      self.target = pygame.sprite.Group()

      #Snake
      self.snake = pygame.sprite.Group()

      #Font
      self.font_name = pygame.font.Font('assets/blackhansans.ttf', 23)
      self.font_end = pygame.font.Font('assets/blackhansans.ttf', 30)
      self.font_game = pygame.font.Font('assets/blackhansans.ttf', 20)

      #User name
      self.name = ""
      self.ask = "Name"
      
      self.name_count = random.randrange(1, 100)
      self.color_active = pygame.Color('whitesmoke')
      self.color_passive = pygame.Color('black')
      self.color = self.color_passive
      
      self.name_input = False
      
      #State of program
      self.state = "INTRO"
      
      self.difficulty = ""


   def mainLoop(self):
      """
      Controls the state of the game
      args: self
      return: none
      """
      while self.state:
         if self.state == "INTRO":
            self.introLoop()

         elif self.state == "MODE":
            self.modeLoop()

         elif self.state == "GAME":
            self.gameLoop()
         
         elif self.state == "END":
            self.endLoop()
   
   def introLoop(self):
      """
      Controls the introduction/start screen when the program is initially run
      args: self
      return: none
      """
      play_button = src.button.Button(160, 100, 280, 50, (204, 0, 0), (0, 0, 0), "PLAY", 30)
      leaderboard_button = src.button.Button(160, 160, 280, 50, (204, 0, 0), (0, 0, 0), "LEADERBOARD", 30)
      rules_button = src.button.Button(160, 220, 280, 50, (204, 0, 0), (0, 0, 0), "RULES", 30)
      quit_button = src.button.Button(10, 330, 100, 50, (204, 0, 0), (0, 0, 0), "QUIT", 20)
      
      name_ask = self.font_game.render(self.ask, True, (204, 0, 0))
      name_ask_rect = name_ask.get_rect()

      self.screen.blit(self.intro_background, (0,0))
      
      self.screen.blit(play_button.image, play_button.rect)
      self.screen.blit(leaderboard_button.image, leaderboard_button.rect)
      self.screen.blit(rules_button.image, rules_button.rect)
      self.screen.blit(quit_button.image, quit_button.rect)
      
      self.screen.blit(name_ask, name_ask_rect)

      pygame.display.update()

      while self.state == "INTRO":
         Controller.gameEventLoop(self)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.state = "END"
      
         mouse_pos = pygame.mouse.get_pos()
         mouse_pressed = pygame.mouse.get_pressed()

         if play_button.is_pressed(mouse_pos, mouse_pressed):
            self.state = "MODE"
            self.modeLoop()

         if leaderboard_button.is_pressed(mouse_pos, mouse_pressed):
            self.state = "LEADERBOARD"
            self.leaderboardLoop()

         if rules_button.is_pressed(mouse_pos, mouse_pressed):
            self.state = "RULES"
            self.rulesLoop()

         if quit_button.is_pressed(mouse_pos, mouse_pressed):
             self.state = "END"
             self.endLoop()

         if self.name_input == True:
            self.color = self.color_active
         
         elif self.name_input == False:
            self.color = self.color_passive
         
         self.name_text = src.name.Name(self.screen, self.color, self.name, 0, 25, 160, 34)

         pygame.display.flip()
         

   def gameLoop(self):
      """
      Controls the game aspect of the program
      args: self
      return: none
      """

      if self.difficulty == "EASY":
         for i in range(4):
            self.target.add(src.target.Target(self.width, self.height, self.target_height_easy , self.target_height_easy))
         
      elif self.difficulty == "HARD":
         for i in range(4):
            self.target.add(src.target.Target(self.width, self.height, self.target_width_hard , self.target_height_hard))
         
         for i in range(2):
            self.snake.add(src.snake.Snake(self.width,self.height))
         
      elif self.difficulty == "PRO":
         for i in range(4):
            self.target.add(src.target.Target(self.width, self.height, self.target_width_pro, self.target_height_pro))
         
         for i in range(2):
            self.snake.add(src.snake.Snake(self.width,self.height))            
      
      while self.state == "GAME":
         pygame.mouse.set_visible(False)

         self.name_input = False

         self.gameEventLoop()
         
         text_timer = self.font_game.render(self.timer_string.rjust(3), False, (255, 255, 255))
         text_score = self.font_game.render(self.score_string.rjust(3), False, (255, 255, 255))
         text_accuracy = self.font_game.render(self.accuracy_string.rjust(3), False, (255, 255, 255))

         update_text_timer = self.screen.blit(text_timer, (160, 0))
         update_text_score = self.screen.blit(text_score, (0, 0))
         update_text_accuracy = self.screen.blit(text_accuracy, (435, 0))

         pygame.display.update(update_text_timer)
         pygame.display.update(update_text_score)
         pygame.display.update(update_text_accuracy)
         
         self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
         self.reticle.update(self.mouse_x,self.mouse_y)
         
         self.screen.blit(self.game_background, (0,0))         

         pygame.sprite.groupcollide(self.target, self.snake, False, True)

         if self.difficulty == "EASY":
            if len(self.target) < 4:
               self.target.add(src.target.Target(self.width, self.height, self.target_height_easy , self.target_height_easy))

         elif self.difficulty == "HARD":
            if len(self.target) < 4:
               self.target.add(src.target.Target(self.width, self.height, self.target_width_hard , self.target_height_hard))
            
            if len(self.snake) < 2:
               self.snake.add(src.snake.Snake(self.width,self.height))
         
         elif self.difficulty == "PRO":
            if len(self.target) < 4:
               self.target.add(src.target.Target(self.width, self.height, self.target_width_pro, self.target_height_pro))    
            
            if len(self.snake) < 4:
               self.snake.add(src.snake.Snake(self.width,self.height))

         self.snake.draw(self.screen)
         self.target.draw(self.screen)
        
         self.reticle.draw(self.screen)
                  
         if self.timer == 0:
            self.state = "ENDSCREEN"
            self.gameoverLoop()

         pygame.display.flip()
         

   def gameEventLoop(self):
      """
      Sets and controls the events that take place in the program
      args: self
      return: none
      """
      for event in pygame.event.get():
         mouse_pos = pygame.mouse.get_pos()
         mouse_pressed = pygame.mouse.get_pressed()
         if self.state == "INTRO":
            if event.type == pygame.MOUSEBUTTONDOWN:
               if self.name_text.is_pressed(mouse_pos, mouse_pressed):
                  self.name_input = True
               
               else:
                  self.name_input = False

            if event.type == pygame.KEYDOWN:
               if self.name_input == True:
                  if event.unicode.isalpha():
                     if len(self.name) < 12:
                        self.name += event.unicode
                     
                     else:
                        self.name[:-1]

                  elif event.key == pygame.K_BACKSPACE:
                     self.name = self.name[:-1]
         
         elif self.state == "GAME":
            if event.type == pygame.USEREVENT:
               self.timer -= 1
               self.snake.update()
               self.timer_string = "Time Remaining: {}".format(self.timer)
               self.clock.tick(60)

            if event.type == pygame.MOUSEBUTTONDOWN:
               self.gunshot.play()
               self.clicks += 1
               self.accuracy = round((self.score * 100) / self.clicks)
               
               
               shoot_target = pygame.sprite.groupcollide(self.reticle, self.target, False, True)

               if shoot_target:
                  self.score += 1
                  self.score_string = "Score: {}".format(self.score)
                  
                  self.accuracy = round((self.score * 100) / self.clicks)
               
               if self.difficulty == "EASY":
                  if shoot_target:
                     self.target.add(src.target.Target(self.width, self.height, self.target_width_easy, self.target_height_easy))
               
               if self.difficulty == "HARD":
                  if shoot_target:
                     self.target.add(src.target.Target(self.width, self.height, self.target_width_hard, self.target_height_hard))
               
               if self.difficulty == "PRO":
                  if shoot_target:
                     self.target.add(src.target.Target(self.width, self.height, self.target_width_pro, self.target_height_pro))

               shoot_snake = pygame.sprite.groupcollide(self.reticle, self.snake, False, True)
               
               if shoot_snake:
                     self.snake.add(src.snake.Snake(self.width, self.height))
                     if self.score > 0:
                        self.score -= 1
                        self.score_string = "Score: {}".format(self.score)
                     
                     else:
                        if self.clicks == 1:
                           self.score_string = "Score: {}".format(self.score)
                        
                        else:
                           self.score_string = "Score: {}".format(self.score)
               
               self.accuracy_string = "Accuracy: {}%".format(self.accuracy)            
            
            if event.type == pygame.QUIT:
               self.state = "END"

   def modeLoop(self):
      """
      Controls the different game modes (easy, hard, pro)
      args: self
      return: none
      """
      easy_button = src.button.Button(110, 160, 130, 80, (204, 0, 0), (0, 0, 0), "EASY", 30)
      hard_button = src.button.Button(340, 160, 130, 80, (204, 0, 0), (0, 0, 0), "HARD", 30)
      pro_button = src.button.Button(230, 275, 130, 80, (204, 0, 0), (0, 0, 0), "PRO", 30)
      back_button = src.button.Button(345, 370, 200, 40, (204, 0, 0), (0, 0, 0), "BACK", 20)
      self.name_input = False
      
      while self.state == "MODE":
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.state = "END"
    
         mouse_pos2 = pygame.mouse.get_pos()
         mouse_pressed2 = pygame.mouse.get_pressed()

         if back_button.is_pressed(mouse_pos2, mouse_pressed2):
            self.state = "INTRO"
            self.introLoop()

         if easy_button.is_pressed(mouse_pos2, mouse_pressed2):
            self.difficulty = "EASY"
            
            self.state = "GAME"
            self.gameLoop()

         if hard_button.is_pressed(mouse_pos2, mouse_pressed2):
            self.difficulty = "HARD"
            
            self.state = "GAME"
            self.gameLoop()

         if pro_button.is_pressed(mouse_pos2, mouse_pressed2):
            self.difficulty = "PRO"

            self.state = "GAME"
            self.gameLoop()

            

         self.screen.blit(self.difficulty_background, (0,0))
         self.screen.blit(easy_button.image, easy_button.rect)
         self.screen.blit(hard_button.image, hard_button.rect)
         self.screen.blit(pro_button.image, pro_button.rect)
         self.screen.blit(back_button.image, back_button.rect)

         pygame.display.update()
   
   def leaderboardLoop(self):
      """
      Controls the leaderboard screen
      args: self
      return: none
      """
      if self.name == "":
         self.name = "Player {}".format(self.name_count)
      back_button = src.button.Button(345, 370, 200, 40, (255, 150, 1), (0, 0, 0), "BACK", 20)
      self.leaderboard = src.leaderboard.Leaderboard('src/leaderboard.json', self.name, self.score, self.width, self.height, self.difficulty)
      
      self.leaderboard.entry()
      self.leaderboard.sort()
      self.screen.blit(self.leaderboard_background, (0,0))
      self.screen.blit(back_button.image, back_button.rect)


      self.leaderboard.update() 
      while self.state == "LEADERBOARD":
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.state = "END"
               self.endLoop()

         mouse_pos = (pygame.mouse.get_pos())
         mouse_pressed = pygame.mouse.get_pressed()

         if back_button.is_pressed(mouse_pos, mouse_pressed):
            Controller.__init__(self, width=600, height=400)
            self.introLoop()
         pygame.display.update()
    
   def rulesLoop(self):
      """
      Changes the screen to show the rules of the game
      args: self
      return: none
      """
      back_button = src.button.Button(345, 370, 200, 40, (204, 0, 0), (0, 0, 0), "BACK", 25)
 
      self.screen.blit(self.rules_background, (0,0))
      self.screen.blit(back_button.image, back_button.rect)
      while self.state == "RULES":
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.state = "END"
               self.endLoop()

         mouse_pos = (pygame.mouse.get_pos())
         mouse_pressed = pygame.mouse.get_pressed()

         if back_button.is_pressed(mouse_pos, mouse_pressed):
            Controller.__init__(self, width=600, height=400)
            self.introLoop()

         pygame.display.update()

   def gameoverLoop(self):
      """
      Controls the end-game screen when the game is over
      args: self
      return: none
      """
      self.state = "ENDSCREEN"
      pygame.mouse.set_visible(True)
      
      playagain_button = src.button.Button(50, 270, 200, 50, (159, 218, 239), (0, 0, 0), "PLAY AGAIN", 25)
      leaderboard_button = src.button.Button(330, 270, 200, 50, (159, 218, 239), (0, 0, 0), "LEADERBOARD", 25)
      quit_button = src.button.Button(190, 340, 200, 50, (159, 218, 239), (0, 0, 0), "QUIT", 25)

      text_score = self.font_end.render(self.score_string.rjust(3), True, pygame.Color('blue'))
      text_score_rect = text_score.get_rect(x = 230, y = 120)

      text_accuracy = self.font_end.render(self.accuracy_string.rjust(3), True, pygame.Color('blue'))
      text_accuracy_rect = text_accuracy.get_rect(x = 180, y = 150)

      self.screen.blit(self.endscreen_background, (0,0))
      self.screen.blit(playagain_button.image, playagain_button.rect)
      self.screen.blit(leaderboard_button.image, leaderboard_button.rect)
      self.screen.blit(quit_button.image, quit_button.rect)

      self.screen.blit(text_score, text_score_rect)
      self.screen.blit(text_accuracy, text_accuracy_rect)

      while self.state == "ENDSCREEN":
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.state == "END"
               self.endLoop()

         mouse_pos = pygame.mouse.get_pos()
         mouse_pressed = pygame.mouse.get_pressed()

         if playagain_button.is_pressed(mouse_pos, mouse_pressed):
            Controller.__init__(self, width=600, height=400)
            self.introLoop()

         if leaderboard_button.is_pressed(mouse_pos, mouse_pressed):
            self.state = "LEADERBOARD"
            self.leaderboardLoop()

         if quit_button.is_pressed(mouse_pos, mouse_pressed):
             self.state = "END"
             self.endLoop()

         pygame.display.update()

   def endLoop(self):
      """
      Allows the user to exit the program
      args: self
      return: none
      """
      pygame.quit()
      sys.exit()

      