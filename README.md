# Paddy's Blackjack

This Python project is a command-line implementation of the classic casino card game Blackjack. It allows players to enjoy the excitement of playing Blackjack right from their terminal.

Deployed project can be found here: [Deployed Project](https://paddysblackjack.herokuapp.com)

![Responsice Mockup](https://i.imgur.com/A1sz8Gk.png)

## Features 

- Player Interaction: Players can participate in the game by making decisions such as hitting, standing, or doubling down.
- Dealer AI: The dealer follows a set of rules to determine its actions, creating a challenging and realistic gameplay experience.
- Scoring System: The game keeps track of each player's score and displays it at the end of each round.
- Game Statistics: Detailed statistics are provided, including the number of wins, losses, and ties for each player.

## How to Play

+ Run the Python script on your terminal.
+ Follow the on-screen instructions to set up the game parameters, such as the number of players and their names.
+ Place your bets and start playing by making decisions based on the options presented.
+ The dealer will deal the initial cards, and players can choose to hit (draw a card), stand (end their turn), or double down (double their bet and draw one more card).
+ The dealer will reveal their cards and follow the predefined rules for drawing additional cards.
+ The round ends, and the results are displayed, including the winner(s) and their respective scores.
+ Players can choose to continue playing or exit the game.

## Requirements
+ Any WebBrowser.
+ Python
### Existing Features

- __Rules__

    - When the game starts, the player gets asked if they want to read the rules.

     

    ![Read The Rules](https://i.imgur.com/Zu1CyKk.png)
    ![Rules Text](https://i.imgur.com/fSRtaey.png)

- __Score__

  - The score is always updated when the match is over, it's presented to player when the match is over.

  ![Score](https://i.imgur.com/zIpTJBw.png)




### Features Left to Implement

- Betting fictional money and Player Against Player.

## Testing 

### Validator Testing 

- Using the PEP8CI Python validator, no errors found

[Validator](https://i.imgur.com/rf6HYNy.png)
    

### Unfixed Bugs

All the bugs were previously fixed. No new bugs found

## Deployment

The Program was deployed in Heroku.
 
1.  Log in to your Heroku account and access the dashboard.
2.  Look for the "New" button and click on it to create a new app.
3.  Provide a unique name for your app, select the region that is  closest to you, and click "Create app."
4.  In the app's settings, locate the "Reveal Config Vars" button and click on it.
5. Create a configuration variable "API_URL" and the value "https://tasty.p.rapidapi.com/recipes/list"
6.  Get your API key and create a configuration variable "API_KEY" and complete the value with your key.
7.  Create another configuration variable "PORT" and the value to "8000," and click "Add."
8.  To specify the dependencies for your app, go to the "Add Buildpack" section.
9.  Select "Python" as the first dependency and "Node.js" as the second. The order of the dependencies is crucial.
10.  Navigate to the "Deploy" tab and choose "GitHub" as the deployment method.
11.  Connect your Heroku account to your GitHub account and select the repository you want to deploy.
12.  Enable the "Automatic Deploy" option if you want Heroku to rebuild your project automatically every time you push a new commit.

## Technologies Used
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
  
  - I developed the program using Python.
  


 -  [GitHub](https://github.com/join/welcome) and [Git](https://git-scm.com/) were used to document the development process
  - [Heroku](https://www.heroku.com/) was used for deployment.
  - [PEP8CI](https://pep8ci.herokuapp.com/) was used to validate Python code.
  -  [StackEdit](https://stackedit.io/) to write README
  - [VSC IDE](https://code.visualstudio.com/) 


## Credits

- Code institute student program
- StackOverFlow - For helping me to find a way to solve problems when stuck with one.
- Slack Community - For giving my support and testing the game and looking for bugs
- Victor Miclovich - My menthor supplied by Code Institute. Helped me to identify some problems in my code and fix them.

