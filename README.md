# Computer_Science_Project
Checkers game in Python with AI

## About
This is a checkers game implemented in Python using Pygame and Object-Oriented Programming. The game features:
- 8x8 board with diagonal movement mechanics
- Two-player mode (PvP)
- Single-player mode against AI
- Draw detection when no valid moves available
- King pieces with enhanced movement
- Modern purple and green color scheme

## Installation and Usage
1. Clone the repository
```bash
git clone https://github.com/hoainam1401/Computer_Science_Project.git
cd Computer_Science_Project
```

2. Install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the game:
- **Player vs Player**: `python main.py pvp`
- **Player vs AI**: `python main.py cpu [depth]`

## Game Modes

### Two Player (PvP)
Play against another human player locally. Purple pieces move first, followed by green pieces.

### Single Player (vs AI)
The AI uses the minimax algorithm to make optimal moves. You can adjust the AI difficulty by changing the search depth:

```bash
python main.py cpu 3
```

- **Depth 1** (default): Fast, makes basic moves
- **Depth 3-4**: Moderate difficulty, thinks several moves ahead
- **Depth 5+**: Challenging, but slower to compute

The depth parameter controls how many moves ahead the AI calculates. Higher depth = smarter AI but longer thinking time.

## Game Rules
- **Purple pieces** start at the bottom, **Green pieces** at the top
- Pieces move diagonally forward one square
- Capture opponent pieces by jumping over them
- Pieces become **Kings** when reaching the opposite end (shown with crown)
- Kings can move diagonally in any direction
- **Win conditions**: 
  - Capture all opponent pieces
  - Opponent has no valid moves (draw)

## Testing
Run the test suite:
```bash
python -m unittest discover test
```

Run specific test file:
```bash
python -m unittest test.test_board
```

## Project Structure
```
checkers/          # Core game logic
├── board.py       # Board management and move validation
├── game.py        # Game state and UI rendering
├── piece.py       # Piece class with rendering
└── constants.py   # Colors, dimensions, and assets

minimax/           # AI implementation
└── algorithm.py   # Minimax with alpha-beta pruning

test/              # Unit tests
├── test_board.py  # Board logic tests
├── test_piece.py  # Piece tests
└── test_ai.py     # AI algorithm tests

main.py            # Entry point and game loop
```

## Screenshots
![Screenshot of the game](https://github.com/hoainam1401/Computer_Science_Project/blob/main/preview/Screenshot.png)
