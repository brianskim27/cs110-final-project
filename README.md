# CS110 Project Proposal
# Aim Trainer Game
## CS 110 Final Project
### Fall 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://github.com/bucs110a0fall21/final-project-aimbot

https://docs.google.com/presentation/d/1XZloWv-CC31v5rcEynOM4iazxAhR-DGWxFXN27eFiCw/edit?usp=sharing

### Team: AimBot
#### Brian Kim, Andy Luna, Sung Chan Kang

***

## Project Description *(Software Lead)*
Our project is a 2d shooter game where the goal is to shoot as many targets as possible on the screen in 60 seconds. Each time a target is shot, a new one appears in a different, random location and the user is awarded one point. In Hard and Pro difficulties, there are snakes that appear, which if shot, deduct points by one and reduces the accuracy stat. Missing a target also results in a reduction in accuracy. The game also consists of a leaderboard that stores and shows the top five scores (and respective user names) in each difficulty, Easy, Hard, and Pro.

***    

## User Interface Design *(Front End Specialist)*
*  ![image](https://user-images.githubusercontent.com/89826657/140571601-f3512ee6-af97-43eb-af3b-f9733f99f8fe.jpeg) - This is the main page of the game after a possible log-in process. It includes a leaderboard, a button that takes the user to the rules and how to play screen, a setting and preferences button, a stats button which shows them how they've been performing in the game, and a start game button which allows them to choose the dificulty. 
   ![image](https://user-images.githubusercontent.com/89826657/140572607-4b61fe2d-1298-4efa-b700-b1d970586d43.jpeg) - This is what an in-game screenshot would look like. The purpose of the game is attempting to shoot the blue squares while avoiding the red circles. When the user shoots a blue target, score will be added and another square will apear on the screen. The amount of red circles that will elimnate points will depend on the difficulty. 
   ![image](https://user-images.githubusercontent.com/89826657/140572666-57055b42-6a92-4d99-8622-4f9dfca42b95.jpeg) - The pause pop-up allows the user to access their settings and controls, the rules, and a quit game functionality that will take them to the main page. 
   ![image](https://user-images.githubusercontent.com/89826657/140572881-7aa12fd7-524c-4a55-b97b-17bf456b845d.jpeg) - The Training Over screen shows the user their score and accuracy followed by a graph of their past scores. 

![image](https://user-images.githubusercontent.com/89826657/145326961-be6efbb4-a580-44b7-aeb0-683a29d5431f.png)
![image](https://user-images.githubusercontent.com/89826657/145326994-015a9d33-baa6-4712-96b0-7270db1e3961.png)
![image](https://user-images.githubusercontent.com/89826657/145326972-1722269b-a2ba-4512-b70d-172dd645809c.png)
![image](https://user-images.githubusercontent.com/89826657/145326977-c44896ec-0709-43e6-9ccd-fb402bf0673b.png)
![image](https://user-images.githubusercontent.com/89826657/145327241-904fede0-4081-4569-a817-6b0ac7a3d1f0.png)
![image](https://user-images.githubusercontent.com/89826657/145327035-a7582994-8bed-4cf6-8fe5-d98648f8cd23.png)

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Pygame Library
        * https://www.pygame.org/news
        * You can use drawings, sprites, sounds, and more in order to make something. This was the main library we used in order to make the game work.

* Class Interface Design
    *
        * https://docs.python.org/3/library/random.html

    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![image](https://docs.google.com/drawings/d/1oR4T2mmiUbqtwIS4UkccqGYdqeqIJzNsBQmbW2r-Z3A/edit)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * Snake:
         * The class loads an image, scales it, and updates the image we picked(pygame mascot) on different parts of the screen every second. This would then be used to check if you clicked on it, resulting in a loss of points. 
    * Target:
         * The class does the same as the Snake class but instead of a snake, we have a target as the iamge. Whenever this target is clicked on, it would add points to the users score. 
    * Reticle:
         * This class would be used to get the location of the cursor to update the image of a reticle we picked.
    * Button:
         * This class was used to create buttons that can be clicked on.
    * Leaderboard:
         * This class was used in order to get the score of a user and add it to a json file that can keep data and display the top 5 scores for each gamemode.
    * Name:
         * This class would create a textbox so that if it is clicked, the user can add their name
    * Controller:
         * This class would update everything and go through different loops based on the state of the game.
## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* README.md
* demo.mp4
* bin
    * button.py
    controller.py
    leaderboard.json
    leaderboard.py
    name.py
    reticle.py
    snake.py
    target.py
* assets
    * blackhansans.ttf
    class_diagram.jpg
    difficulty.jpeg
    gamebackground.jpg
    gameoverscreen.jpeg
    introbackground.jpeg
    leaderboard.jpeg
    reticle.png
    rulesscreen.jpeg
    snake.png
    sound.wav
    target.png
* etc
    * None

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Brian Kim

Software lead facilitated collaboration and communication among group members and assisted both the front and back end specialists with any confusions or struggles. Worked on Controller, Name, Reticle, Snake, Target, and Leaderboard classes.

### Front End Specialist - Sung Chan Kang

Front-end lead conducted research on working with GUI and subsequently created different screens and added images for sprites, rectangles, and backgrounds through the Controller class. Also created the Button class.

### Back End Specialist - Andy Luna

Back-end lead worked on creating the functionality of the game, creating and working on Leaderboard, Reticle, Snake, and Target classes. Conducted research on json to create a working leaderboard system.

## Testing *(Software Lead)*
* Everytime something new was added to the project, I tested it by either using the print function to check whether the command runs properly, adding, removing, or changing values to visualize it, or moving around the order of lines to verify whether it should go before or after some code.
    * For example, I used the print function to test whether clicking the name box was working or not. Everytime I clicked on the box, the program printed out "True", and everytime I clicked outside of the box, the program printed out "False." This allowed me to verify whether the program was running the code where the mouse is touching (collide) the box, and if the box gets clicked or not.

* Your ATP

| Step                  | Action     |  Result  | 
| ----------------------|:-------------:| -----------------:|
|  1  | Run Aim Trainer program  | GUI window appears with 'Introduction' screen displayed |
|  2  | Click 'Rules' button  | Display changes to 'Rules' screen |
|  3  | Click 'Back' button on 'Rules' screen  | Display returns to 'Introduction' screen |
|  4  | Click 'Leaderboard' button  | Display changes to 'Leaderboard' screen |
|  5  | Click 'Back' button on 'Leaderboard' screen  | Display returns to 'Introduction' screen |
|  6  | Click on top-left box below 'Name' and type out name (max 12 chars) | Display adds letters of inputted name inside the box |
|  7  | Click 'Play' button  | Display changes to 'Difficulty' screen |
|  8  | Click on 'Easy' button  | Display changes to 'Game' screen and loads in a score count, active timer, and accuracy count on the top, four targets, and a reticle following the mouse |
|  9  | Click on targets | Program plays a gunshot sound, clicked targets reappear at random locations on the screen, score count increases, accuracy increases (if less than 100%) |
|  10  | Click on an empty part of screen  | Program plays a gunshot sound, accuracy decreases |
|  11  | Play until timer reaches 0  | Display changes to 'End' screen |
|  12  | Click 'Leaderboard' button  | Display changes to 'Leaderboard' screen |
|  13  | Click 'Back' button  | Display changes to 'Introduction' screen |
|  14  | Go to 'Difficulty' screen and click 'Hard' button  | Display changes to 'Game' screen and additioanlly loads in two snakes and decreases size of targets |
|  15  | Click on snakes  | Program plays a gunshot sound, clicked snakes reappear at random locations on the screen, score count decreases, accuracy decreases (if greater than 0) |
|  16  | Reach 'End' screen and click 'Play Again' button  | Display changes to 'Introduction' Screen|
|  17  | Go to 'Difficulty' screen and click 'Pro' button  | Display changes to 'Game' screen and additioanlly loads in four snakes and further decreases size of targets|
|  18  | Reach 'End' screen and click 'Exit' button  | GUI window closes and program ends|
