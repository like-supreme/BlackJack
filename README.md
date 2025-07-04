# BlackJack
Blackjack game using python functions, loops and lists
# 🃏 Blackjack - Python Terminal Game

This is a simple **Blackjack** game that runs in the terminal, written entirely in Python. You play against the dealer, trying to get as close to 21 as possible without going over.

## 🚀 How It Works

1. Both the player and dealer are dealt 2 cards at the start.
2. The player can choose to "Hit" (draw a card) or "Stand" (stop drawing).
3. The dealer automatically draws until their hand total is 17 or higher.
4. After the round ends, scores are compared and the winner is declared.

## ✨ Features

- Realistic card values (11 = Ace, face cards = 10)
- Automatic Ace value adjustment (11 ➝ 1 if needed)
- Dealer logic follows official Blackjack rules
- Continuous play support (ask to play again)
- ASCII logo using `art.py`
- Game logic fully modularized in `play_the_game_function.py`

## 📁 File Structure

blackjack/
├── main.py # Entry point of the game
├── play_the_game_function.py # Main game logic
└── art.py # Logo artwork

## ▶️ Getting Started

1. Make sure you have Python 3 or later installed.
2. Clone this repository or download the files.
3. Run the game

 Tech Used
Python 3.7.9

ASCII art for logo

Simple terminal input/output

🂡 🂠 Welcome to Blackjack!
Your cards: [10, 1]
Dealer's first card: 9
Want to draw another card? y/n? y
...


## 📦 Features

- Fully functional command-line Blackjack game
- Score calculation with Ace (`11 or 1`) handling
- Dealer draws until reaching a minimum of 17
- Game automatically compares hands and declares the winner
- Replayable game loop with clean restart
- Modular structure (game logic separated into `play_the_game_function.py`)





