## Table of Contents

  - [Introduction](#Introduction)
  - [UX](#ux)
    - [Strategy](#strategy)
      - [Main Goal](#main-goal)
    - [User Needs](#user-needs)
      - [Scope](#scope)
    - [Design and Logic Flow Chart](#Design-and-Logic-Flow-Chart)
    - [app.diagrams.net](#diagrams)
    - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [Functionality Testing](#functionality-testing)
    - [Testing user needs](#testing-user-needs)
  - [Bugs](#bugs)
  - [Deployment](#Deployment)
  - [Future updates and features](#Future-updates-and-features)
  - [Code and Credits](#Code-and-Credits)


  # BlackJack 

**[LIVE DEMO - Click & Play ](https://black-jack-portofolio3.herokuapp.com/)**


  ![](/images/responsive.PNG)



# Introduction
The North American game of Blackjack, also known as 21, has been one of the most popular casino games of the last hundred years and has spread throughout the world. In the 21st century it has been overtaken in popularity by Slots (slot machine games), but it remains one of the most popular casino card games and is available in almost all casinos both on and offline.

Blackjack is a casino banked game, meaning that players compete against the house rather than each other. The objective is to get a hand total of closer to 21 than the dealer without going over 21 (busting).

At the start of a Blackjack game, the players and the dealer receive two cards each. The players' cards are normally dealt face up, while the dealer has one face down (called the hole card) and one face up. The best possible Blackjack hand is an opening deal of an ace with any ten-point card.

The house advantage of this game is derived from several rules that favour the dealer. The most significant of these is that the player must act before the dealer, allowing the player to bust and lose their bet before the dealer plays.

# UX

#### Main Goal
- Create a card game with basic Python concepts that I as a junior developer understand
- Create and provide the user with a simple blackjack experience without gambling and losing any real money in real life

### User Needs

  #### Scope
  - user can read the rules on the terminal and how to play the game.
  - when you lose or win  to have the option to play again

 ### Testing the game

 # Functionality testing
   - the game  has been tested in gitpod terminal Replit and Heroku terminal
   - tested with all the options available "HIT" , "STAND" features for a simple blackjack experience

 # Testing user needs 
   - The start of the game the user can read the rules and is asked if it wants to play blackjack 

  # Testing the code with PEP8 online
  ![](/images/pep%208.PNG)


 ### Design and Logic Flow Chart
  
- for the flow chart I used [app.diagrams.net] (https://app.diagrams.net)


![](/images/Capture.PNG)


#### Technologies Used
- Python
- Heroku
- GitHub
- GitPod
- app.diagrams.net
- ASCII art 


### Bugs

- trailing  white spaces ;fixed by removing extra space
- indenation errors  which broke my while loops few times
- line to long errors 


### Deployment

- create an account with Heroku
- fork or clone this repository
- ensure that the Profile is in place
- create a new app in Heroku
- select "New" and "Create new app"
- add name for the app and press "Create new app"
- in "Settings" select "BuildPack" and select Python and Node.js
- in "Settings" click "Reveal Config Vars" and input the fallowing key : PORT,VALUE:8000.
- press on "Deploy" and select your method and repository
- press "Connect" on selected Github repository
- choose beween "Enable Automatic Deploys" or Deploy Branch" in the manual deploy section
- Heroku will now deploy it to the site

### Future updates and features

 - On the future I would like to add a "High Score" feature , where players can see and store their high scores against the computer.
 - I would like add real casino mechanics and player strategies like "Split", If you hold two cards that are the same number in your hand, like two eights or two sixes, you can split them apart and play each one like two separate hands instead of one. Once    you split your two cards into two hands, you’ll place your original bet with one hand and place an equal bet on the second, split hand.
  You will play the hand to your right first. The dealer will give you a card when you ask for a “hit.” You will continue to hit until you are satisfied or you bust.
  Then, you move to play the other hand and have the dealer hit you with cards until you say “stop” or you go over 21. If you go over 21, you lose your bet on that hand.
 If you have a pair of aces and split them, the dealer will give you only one additional card per hand. You cannot draw again. If you draw a 10 on the second card, you have 21. Your winning hand pays 1:1, not 3:2 like other winning blackjack hands.
 - "Double Down" mechanic where on your original two cards, you can double your bet before the  dealer gives you another card. You place another bet equal to the first. Then, the dealer will give you only one card The dealer settles all bets at the end of the  hand.
  If you have sevens, you can split a pair, as above, and double down if you want to.
 - I would like to add casino chips and a betting system  
 - I would like to add real cards pictures and casino theme with css and html 
 - I would like to add casino sounds 


### Code and Credits

 - Project inspiration [Washington Post] (https://games.washingtonpost.com/games/blackjack/)
 - Love Sandwhices project @ Code institute for a laying a general code knowledge on the foundation
 - Huge help from the Slack community on helping me out with gitpod indentation
 - Python community on the discord app , where I got help with the logic of the game
 - Stack Overflow for logic and understanding python concepts better  
 - My Mentor Dario for the great support and help