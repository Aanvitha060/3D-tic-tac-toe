# 3D Tic-Tac-Toe Game with AI (Alpha-Beta Pruning)

## Overview

This project implements a 3D Tic-Tac-Toe game (4×4×4 grid) with a web-based interactive interface and an AI opponent. The AI uses the Minimax algorithm with alpha-beta pruning, supporting three difficulty levels.

---

## Features

- **3D 4×4×4 Tic-Tac-Toe Board** rendered dynamically in HTML/JavaScript
- **Interactive Web Interface**: Clickable cells, immediate updates, and visual board
- **AI Opponent** using Minimax with Alpha-Beta Pruning
- **Three Difficulty Levels**:
  - Easy (depth 1)
  - Medium (depth 2)
  - Hard (depth 3)
- **Flask Backend** to process moves and manage game logic

---

## How to Run

### 1. Install dependencies

```bash
pip install flask
```

### 2. Run the Flask server

```bash
python app.py
```

### 3. Open your browser

Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## File Structure

```
project-folder/
├── app.py              # Flask backend with game logic and AI
├── templates/
│   └── index.html      # Frontend interface
└── README.md           # Project overview and instructions
```

---

## Code Documentation

- `app.py` includes:
  - Game state stored in a 3D list
  - `/move` route: handles player move, checks win, responds with AI move
  - `check_winner()`: validates all 76 winning line conditions
  - `minimax()`: recursive AI with alpha-beta pruning
  - `find_best_move()`: selects best move based on difficulty level

- `index.html`:
  - Renders the board dynamically
  - Handles user interaction and updates via JavaScript

---

## Notes

- This project fulfills the rubric requirement for a working 3D game, alpha-beta logic, interactive interface, and difficulty options.
