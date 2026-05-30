Hangman Game

Overview

Hangman Game is a simple text-based Python game where one player enters a secret word and another player tries to guess it one letter at a time.

The player has a maximum of 6 incorrect guesses to identify the word. The game provides feedback for correct and incorrect guesses and displays the current progress after each attempt.

Features

- Text-based console game
- Dynamic secret word input
- Letter-by-letter guessing
- Maximum of 6 wrong attempts
- Input validation
- Prevents duplicate guesses
- Win and lose conditions

Technologies Used

- Python 3

Concepts Used

- Strings
- Lists
- While Loop
- If-Else Statements
- User Input and Output

How to Run

1. Clone the repository:

git clone https://github.com/your-username/hangman-game.git

2. Open the project folder:

cd hangman-game

3. Run the Python file:

python hangman.py

Sample Output

Enter the secret word: python

🎮 Welcome to Hangman!

Word: _ _ _ _ _ _
Wrong guesses left: 6

Enter a letter: p
✅ Correct!

Word: p _ _ _ _ _

Enter a letter: y
✅ Correct!

Word: p y _ _ _ _

...

🎉 Congratulations! You guessed the word: python

Project Structure

hangman-game/
│
├── hangman.py
└── README.md

Future Improvements

- Random word selection
- Difficulty levels
- Score tracking
- Multiple rounds
- Graphical User Interface (GUI)
