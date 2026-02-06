# Tic-Tac-Toe AI
**Name:** Fares Salem
**Student ID:** T00039863

## Implementation Approach
In this project, I implemented the Tic-Tac-Toe game using the **Minimax Algorithm**. The AI looks ahead at all possible moves to choose the one that leads to a win or a tie, making it unbeatable. I used simple recursive functions like `get_max` and `get_min` to calculate the scores for each board state.

## Challenges
- **Understanding Recursion:** At first, it was hard to understand how the Minimax function calls itself, but I solved this by tracing the moves on paper.
- **Deep Copying:** I learned that I must use `copy.deepcopy()` so the AI doesn't mess up the actual game board while thinking about future moves.

## How to Run
1. Install pygame: `pip install pygame`
2. Run the game: `python runner.py`
