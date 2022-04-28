import json
import collections
import pygame

class Leaderboard:
    def __init__(self, filename, name, score, width, height, difficulty):
        """
        Initializes a leaderboard
        args: self, filename (str), name (str), score (int), width (int), height (int), difficulty (str)
        return: none
        """
        pygame.init()
        pygame.font.init()  
        self.name = str(name)
        self.score = score
        self.file_name = filename

        self.difficulty = difficulty
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.font_leaderboard = pygame.font.Font('assets/blackhansans.ttf', 15)

    def entry(self):
        """
        Adds an entry into the leaderboard based on name, score, and difficulty
        args: self
        return: none
        """
        if self.difficulty == "EASY":
            self.easy_name_score  = {self.name: self.score}
            with open(self.file_name, "r+") as self.file:
                easy_data = json.load(self.file)
                easy_data['Easy'].update(self.easy_name_score)
                self.file.seek(0)
                json.dump(easy_data, self.file)

        if self.difficulty == "HARD":
            self.hard_name_score = {self.name: self.score}
            with open(self.file_name, "r+") as self.file:
                hard_data = json.load(self.file)
                hard_data['Hard'].update(self.hard_name_score)
                self.file.seek(0)
                json.dump(hard_data, self.file)
  

        if self.difficulty == "PRO":
            self.pro_name_score = {self.name: self.score}
            with open(self.file_name, "r+") as self.file:
                pro_data = json.load(self.file)
                pro_data['Pro'].update(self.pro_name_score)
                self.file.seek(0)
                json.dump(pro_data, self.file)

    def sort(self):
        """
        Sorts the dictionary from highest to lowest scores in the respective modes
        args: self
        return: none
        """
        file = open(self.file_name, 'r')
        dictionary = json.load(file)

        keys, values = zip(*dictionary.items())
        Easy, Hard, Pro = values
        
        #Easy
        easy_name_list = []
        easy_score_list = []
        self.sorted_easy_scores = collections.Counter(Easy).most_common(5)
        for values in self.sorted_easy_scores:
            name , score = values
            easy_name_list.append(name)
            easy_score_list.append(score)    
            
        easy_first = f"1 {easy_name_list[0]} - {easy_score_list[0]}"
        easy_second = f"2 {easy_name_list[1]} - {easy_score_list[1]}"
        easy_third = f"3 {easy_name_list[2]} - {easy_score_list[2]}"
        easy_fourth = f"4 {easy_name_list[3]} - {easy_score_list[3]}"
        easy_fifth = f"5 {easy_name_list[4]} - {easy_score_list[4]}"
        
        #Hard
        hard_name_list = []
        hard_score_list = []
        self.sorted_hard_scores = collections.Counter(Hard).most_common(5)
        for values in self.sorted_hard_scores:
            name , score = values
            hard_name_list.append(name)
            hard_score_list.append(score)    
            
        hard_first = f"1 {hard_name_list[0]} - {hard_score_list[0]}"
        hard_second = f"2 {hard_name_list[1]} - {hard_score_list[1]}"
        hard_third = f"3 {hard_name_list[2]} - {hard_score_list[2]}"
        hard_fourth = f"4 {hard_name_list[3]} - {hard_score_list[3]}"
        hard_fifth = f"5 {hard_name_list[4]} - {hard_score_list[4]}"

        #Pro
        pro_name_list = []
        pro_score_list = []
        self.sorted_pro_scores = collections.Counter(Pro).most_common(5)
        for values in self.sorted_pro_scores:
            name , score = values
            pro_name_list.append(name)
            pro_score_list.append(score)    
            
        pro_first = f"1 {pro_name_list[0]} - {pro_score_list[0]}"
        pro_second = f"2 {pro_name_list[1]} - {pro_score_list[1]}"
        pro_third = f"3 {pro_name_list[2]} - {pro_score_list[2]}"
        pro_fourth = f"4 {pro_name_list[3]} - {pro_score_list[3]}"
        pro_fifth = f"5 {pro_name_list[4]} - {pro_score_list[4]}"

        self.easy_leaderboard = (easy_first,easy_second,easy_third,easy_fourth,easy_fifth)
        self.hard_leaderboard = (hard_first,hard_second,hard_third,hard_fourth,hard_fifth)
        self.pro_leaderboard = (pro_first,pro_second,pro_third,pro_fourth,pro_fifth)

    def update(self):
        """
        Updates the leaderboard screen
        args: self
        return: none
        """
        x_axis_easy = 10
        x_axis_hard = 10
        x_axis_pro = 300
        
        y_axis_easy = 70
        y_axis_hard = 235
        y_axis_pro = 150

        title_easy = self.font_leaderboard.render("Easy", True, pygame.Color('black'))
        title_hard = self.font_leaderboard.render("Hard", True, pygame.Color('black'))
        title_pro = self.font_leaderboard.render("Pro", True, pygame.Color('black'))

        self.screen.blit(title_easy, (x_axis_easy, y_axis_easy))
        self.screen.blit(title_hard, (x_axis_hard, y_axis_hard))
        self.screen.blit(title_pro, (x_axis_pro, y_axis_pro))

        for places in self.easy_leaderboard:
            text_leaderboard_easy = self.font_leaderboard.render(places, True, pygame.Color('black'))
            self.screen.blit(text_leaderboard_easy, (x_axis_easy, y_axis_easy + 20))
            y_axis_easy += 30
        
        for places in self.hard_leaderboard:
            text_leaderboard_hard = self.font_leaderboard.render(places, True, pygame.Color('black'))
            self.screen.blit(text_leaderboard_hard, (x_axis_hard, y_axis_hard + 20))
            y_axis_hard += 30
        
        for places in self.pro_leaderboard:
            text_leaderboard_pro = self.font_leaderboard.render(places, True, pygame.Color('black'))
            self.screen.blit(text_leaderboard_pro, (x_axis_pro, y_axis_pro + 20))
            y_axis_pro += 30
 
 