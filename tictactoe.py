# Name: Fares Salem
# ID: T00039863
# Project: Tic-Tac-Toe AI (Minimax)

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    # Just counting X and O manually
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count = x_count + 1
            if board[i][j] == O:
                o_count = o_count + 1
    
    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    # Find all empty squares and put them in a set
    possible_moves = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible_moves.add((r, c))
    return possible_moves

def result(board, action):
    # Check if move is valid first
    if action not in actions(board):
        raise Exception("Action not possible")

    # Making a copy to not change the original board
    new_board = copy.deepcopy(board)
    p = player(board)
    
    r = action[0]
    c = action[1]
    new_board[r][c] = p
    
    return new_board

def winner(board):
    # Checking rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != None:
            return board[i][0]
            
    # Checking columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != None:
            return board[0][j]
            
    # Checking diagonals one by one
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]
        
    return None

def terminal(board):
    # If there is a winner, the game is over
    if winner(board) != None:
        return True
    
    # Check if the board is full
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                return False
                
    return True

def utility(board):
    # Score calculation
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    # If the game is over, do nothing
    if terminal(board):
        return None
    
    current_p = player(board)
    
    if current_p == X:
        best_val = -1000
        best_act = None
        for move in actions(board):
            score = get_min(result(board, move))
            if score > best_val:
                best_val = score
                best_act = move
        return best_act
    else:
        best_val = 1000
        best_act = None
        for move in actions(board):
            score = get_max(result(board, move))
            if score < best_val:
                best_val = score
                best_act = move
        return best_act

# Simple recursive functions
def get_max(board):
    if terminal(board):
        return utility(board)
    v = -1000
    for move in actions(board):
        res = get_min(result(board, move))
        if res > v:
            v = res
    return v

def get_min(board):
    if terminal(board):
        return utility(board)
    v = 1000
    for move in actions(board):
        res = get_max(result(board, move))
        if res < v:
            v = res
    return v
