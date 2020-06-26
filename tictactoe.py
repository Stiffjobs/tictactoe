"""
Tic Tac Toe Player
"""

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
    """
    Returns player who has the next turn on a board.
    """
    num = 0
    for i in range(3):
        for j in range(3):
           if board[i][j] == None:
               num += 1
               
    #if even O's turn
    if num % 2 == 0:
        return O
    #if odd X's turn
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    x = list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x.append((i, j))
    #print(x)
    return x

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] == EMPTY:
        turn = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = turn
        return new_board
    else:
        raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
        elif board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    #there's no winner now  
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any(None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X: #x is maximizing
        best_Score = -1
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_Score:
                best_Score = value
                best_move = action
        return best_move

    else: #o is minimizing
        best_Score = 1
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_Score:
                best_Score = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = -math.inf

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value