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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count>o_count:
        return O
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty.add((i,j))
    return empty

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise Exception("Canr be None")
    i,j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action: Cell is not empty")
    new_board=copy.deepcopy(board)
    new_board[i][j]=player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0]==row[1]==row[2]!=EMPTY:
            return row[0]
    for j in range(3):
        if board[0][j]==board[1][j]==board[2][j]!=EMPTY:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return EMPTY
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif not actions(board):
        return True
    else:
        return False

    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win==X:
            return 1
        if win==O:
            return -1
        else:
            return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player =player(board)
    def max_value(board):
        if terminal(board):
            return utility(board), None
        v=float('-inf')
        best_action=None
        for action in actions(board):
            min_v,_=min_value(result(board,action))
            if min_v>v:
                v=min_v
                best_action=action
        return v, best_action
    def min_value(board):
        if terminal(board):
            return utility(board), None
        v=float("+inf")
        best_action=None
        for action in actions(board):
            max_v,_=max_value(result(board,action))
            if max_v<v:
                v=max_v
                best_action=action
        return v, best_action
    if current_player==X:
        _,action=max_value(board)
    else:
        _,action=min_value(board)
    return action
    