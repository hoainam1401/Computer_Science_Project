# Agent Guidelines for Checkers Project

## Build/Test Commands
- Run game (PvP): `python main.py pvp`
- Run game (vs AI): `python main.py cpu [depth]` (depth default: 1)
- Run all tests: `python -m unittest discover test`
- Run single test: `python -m unittest test.test_ai.TestMinimaxAlgorithm.test_minimax_max_player`
- Run test file: `python -m unittest test.test_ai`

## Code Style
- **Imports**: Group stdlib, third-party (pygame), then local imports with blank lines between groups
- **Formatting**: Use 4 spaces for indentation, no trailing whitespace
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Classes**: Always include `__init__` method; use private methods with `_` prefix (e.g., `_init`, `_move`, `_traverse_left`)
- **Type hints**: Not currently used in this codebase
- **Error handling**: Use implicit checks (e.g., `if piece != 0`) rather than explicit try/except
- **Constants**: Define in `checkers/constants.py` for colors, dimensions, and pygame assets
- **Default parameters**: Avoid mutable defaults (e.g., use `skipped=[]` becomes `skipped=None` pattern)

## Project Structure
- `checkers/`: Core game logic (Board, Game, Piece classes)
- `minimax/`: AI algorithm implementation
- `test/`: Unit tests using unittest framework
- `main.py`: Entry point with pygame loop
