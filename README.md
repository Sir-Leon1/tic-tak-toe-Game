# Tic-Tac-Toe Game

This project is an implementation of the classic game Tic-Tac-Toe using a command-line interface. It allows two players to take turns marking X and O on a 3x3 grid. The game ends when one player successfully forms a line of three marks horizontally, vertically, or diagonally, or when all the positions on the grid are filled resulting in a draw.
How to Run

## To run the Tic-Tac-Toe game, follow these steps:

    •     Download or clone the repository to your local machine.
    •     Open a terminal or command prompt and navigate to the project directory.
    •     Run the Python script by executing the command: python tic_tac_toe.py
    • Follow the on-screen instructions to play the game.

## Game Rules

    •     The game is played on a 3x3 grid.
    •     Player X always goes first, followed by Player O.
    •     Players take turns entering the position where they want to mark their symbol (X or O) using numbers 1 to 9.
    •     The game ends when one player successfully forms a line of three marks horizontally, vertically, or diagonally.
    •     If all positions on the grid are filled and no player has formed a line, the game ends in a draw.

## Code Structure

The code consists of the following functions:

    •     constboard(board): Prints the current status of the Tic-Tac-Toe board.
    •     user_1_turn(board): Handles the turn of Player X (user input for position).
    •     user_2_turn(board): Handles the turn of Player O (user input for position).
    •     minmax(board, player): Implements the Minimax algorithm for the computer's move decision.
    •     compTurn(board): Determines the computer's turn by calling the minmax function.
    •     analyzeboard(board): Analyzes the current state of the board to determine if a player has won or the game ended in a draw.
    • main(): Main function that controls the flow of the game based on user choices and calls the appropriate functions.

## Game Modes

The Tic-Tac-Toe game offers two modes:

    1. Single Player Mode: Play against the computer.
    2. Multiplayer Mode: Play against another player.

When playing in single-player mode, the computer's moves are determined using the Minimax algorithm, which makes it a challenging opponent.
## Dependencies

The code requires Python to be installed on your system.
Future Improvements

## Possible enhancements to the game could include:

    Implementing a graphical user interface (GUI) for a more interactive experience.
    Adding additional game modes, such as a tournament mode or a time-limited mode.
    Enhancing the computer's AI to provide different difficulty levels for single-player mode.

## Contributions

Contributions to the project are welcome. If you would like to contribute, please follow these steps:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Implement your changes and test them thoroughly.
    Commit your changes with clear and descriptive messages.
    Push your branch to your forked repository.
    Submit a pull request, explaining the purpose and changes made.

## License

This project is licensed under the MIT License.
Acknowledgements

The implementation of the Minimax algorithm in the code is inspired by various resources and tutorials available on game AI and the game of Tic-Tac-Toe.
