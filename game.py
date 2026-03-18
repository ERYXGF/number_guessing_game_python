"""Contains the core game logic. The main game loop lives here: generating the secret number, managing the attempt counter, calling hint functions, checking for win or loss, returning the result. This is the largest file."""
#"Difficulty" Dictionnary that defines each level of difficulty (number of attempts, range and hint precision/thresholds):
difficulty = {
    "easy": {
        "range": (1, 50),
        "attempts": 10,
        "thresholds": [
            (3,  "🔥 Brûlant"),
            (8,  "♨️  Très chaud"),
            (15, "🌡  Chaud"),
            (25, "❄️  Froid"),
        ]
    },
    "medium": {
        "range": (1, 100),
        "attempts": 7,
        "thresholds": [
            (5,  "🔥 Brûlant"),
            (15, "♨️  Très chaud"),
            (30, "🌡  Chaud"),
            (50, "❄️  Froid"),
        ]
    },
    "hard": {
        "range": (1, 200),
        "attempts": 5,
        "thresholds": [
            (10,  "🔥 Brûlant"),
            (30,  "♨️  Très chaud"),
            (60,  "🌡  Chaud"),
            (100, "❄️  Froid"),
        ]
    }
}