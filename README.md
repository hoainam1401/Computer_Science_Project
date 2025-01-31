# Computer_Science_Project
 Checkers game in Python

## About
This is a simple checkers game implemented in Python. The game is played on a 8x8 board and the players can only move diagonally. The game is played between two players and the player who captures all the pieces of the opponent wins the game.
This was made using the Pygame library and OOP.

## Installation and usage
1. Clone the repository
2. Install the required libraries using the following command:
``` pip install -r requirements.txt ```
3. Run the game using the following command:
``` python main.py [cpu|pvp]```. The argument cpu is used to play against the computer and pvp is used to play against another player.

## SinglePlayer 
The AI uses the minimax algorithm with alpha-beta pruning to make the best move. The depth of the tree can be changed when comment in terminal with the following command:
``` python main.py cpu argument```. The argument is the depth of the tree. The default value is 1.
Depth tree is the number of moves the AI can see ahead. The higher the depth, the better the AI plays but it also takes more time to make a move. 

## Screenshots
![Screenshot of the game](https://github.com/hoainam1401/Computer_Science_Project/blob/main/BcSProject/preview/Screenshot.png)
