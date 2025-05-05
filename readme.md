# Ayoayo Game (Text-Based)

Ayoayo is a traditional West African board game centered around strategy, seed-sowing, and capturing. This is a text-based implementation of the game written in Python.

## How to Play

- Two players take turns picking seeds from one of their six pits and distributing them counter-clockwise.
- If the last seed lands in your own empty pit and the opposite pit has seeds, you capture them into your store.
- The game ends when one player's side is empty. Remaining seeds go to the other player’s store.
- The player with the most seeds in their store at the end wins.

## Files

- `main.py` – Entry point of the game. Handles user interaction and flow.
- `game.py` – Contains the core game logic and board management.
- `player.py` – Simple Player class with name and player number.
- `reflection.txt` – Personal reflection on the development process.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repo.
3. Open a terminal in the project directory and run:

   ```bash
   python main.py
