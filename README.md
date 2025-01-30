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
The AI uses the minimax algorithm with alpha-beta pruning to make the best move. The depth of the tree can be changed in the main.py file.
