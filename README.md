# 🎯 Number Guessing Game

A polished command-line number guessing game built in Python with three
difficulty levels, hot/cold proximity hints, directional hints, and a
persistent high score system that tracks your best performance across sessions.

Built as the Month 3 capstone project of a 12-month Python learning roadmap,
this project focuses on control flow, loops, modular file architecture and
JSON persistence.

![demo](assets/demo.gif)

---

## ✨ Features

- Three difficulty levels with distinct ranges and attempt limits
- Higher/lower directional hint after every guess
- Hot/cold proximity hint system with 5 temperature zones scaled per difficulty
- Persistent high score system — best attempt count saved per difficulty
- Session statistics on exit — games played, won and lost
- Full input validation — rejects non-integers and out-of-range values
- Clean menu-driven interface with welcome screen and score viewer

---

## 🎮 Difficulty Levels

| Level  | Range  | Attempts |
|--------|--------|----------|
| Easy   | 1–50   | 10       |
| Medium | 1–100  | 7        |
| Hard   | 1–200  | 5        |

---

## 🌡 Hint System

After every incorrect guess you receive two hints simultaneously:

**Directional** — tells you whether the secret number is higher or lower
than your guess.

**Hot/Cold** — tells you how close you are based on the absolute difference
between your guess and the secret number. Thresholds scale with difficulty
so Hard mode remains challenging throughout.

```
🔥 Brûlant   → Very close
♨️  Très chaud → Close
🌡  Chaud     → Getting there
❄️  Froid     → Far away
🧊  Glacial   → Very far away
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies — standard library only

### Installation & Run

```bash
git clone https://github.com/ERYXGF/number-guessing-game.git
cd number-guessing-game
python main.py
```

---

## 🗂 Project Structure

```
number-guessing-game/
├── main.py             # Entry point — menu loop and session statistics
├── game.py             # Core game loop, difficulty config, random generation
├── hints.py            # Higher/lower and hot/cold hint functions
├── scores.py           # JSON persistence — load, save, check and get records
├── display.py          # All terminal output functions
├── scores_example.json # Sample scores file demonstrating the data structure
├── .gitignore
├── README.md
└── LICENSE
```

---

## 📁 Scores Data Structure

High scores are saved in `scores.json` as a dictionary with one entry
per difficulty level. `null` means no record exists yet for that level:

```json
{
    "easy":   {"best_attempts": 4, "date": "2025-03-17"},
    "medium": {"best_attempts": 6, "date": "2025-03-17"},
    "hard":   null
}
```

---

## 🛠 Built With

- Python 3.11
- Standard library only — `random`, `json`, `datetime`

---

## 📚 What I Learned

- Structuring a project across multiple files with strict separation of concerns
- Using nested dictionaries as a configuration system for game parameters
- Building two-level nested loops — outer for game progression, inner for input validation
- Implementing a proximity hint system with thresholds that scale per difficulty
- Persisting and comparing high scores across sessions using JSON
- Passing return values between functions across different files
- Translating pseudocode into working Python systematically (for each function I created)
- How parameters in function work accross different files
- How to add a file to .gitignore
---

## 🗺 Future Improvements

- [ ] Add a countdown timer per session
- [ ] Add a mathematical hint option that costs one attempt
- [ ] Multiplayer mode — two players alternate guessing
- [ ] Validate all menu inputs against non-integer entries in main.py
- [ ] Colour terminal output using the colorama library

---

## ⚠️ Note

`scores.json` is excluded from version control via `.gitignore`.
`scores_example.json` is included to demonstrate the expected data structure.

---

## 📄 Licence

This project is licensed under the GPL-3.0 Licence.
See the [LICENSE](LICENSE) file for details.

---

*Project 3 of 12 — Python learning roadmap | Built by [Eryx Grammatikas](https://github.com/ERYXGF)*