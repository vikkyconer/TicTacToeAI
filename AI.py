import TicTacToe
import time
import pdb
import cPickle as pickle

discount = 0.3
actions = TicTacToe.actions
Q = {}
move = 0
gen = 0

def maxQ(s):
    val = None
    act = None
    if (s not in Q):
        temp = {}
        for action in actions:
            temp[action] = 0.1
        Q[s] = temp
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val

def do_action(action):
    global move
    s = TicTacToe.board
    r = -TicTacToe.score
    isLost = False
    isWon = False
    isDraw = False
    TicTacToe.print_board(TicTacToe.board)
    f = 0
    if move % 2 == 0:
    	turn = 'X'
        f = TicTacToe.try_move(turn, action)
        if(f == -1):
            r -= TicTacToe.score
            return s, action, r, tuple(s), isLost, isWon, isDraw
    else:
    	turn = 'O'
    	user = raw_input("Where would you like to place " + turn + " (1-9)? ")
    	user = int(user)
        f = TicTacToe.try_move(turn, user)
        while(f == -1):
            user = raw_input("Where would you like to place " + turn + " (1-9)? ")
            user = int(user)
            f = TicTacToe.try_move(turn, user)
    s2 = tuple(TicTacToe.board)
    r -= TicTacToe.score

    move += 1
    if move > 4:
    	winner = TicTacToe.check_win(TicTacToe.board)
    	if winner != -1:
            if winner == 1:
                print 'The winner is X'
                r += TicTacToe.score
                isWon = True
            else:
                print 'The winner is O'
                r -= TicTacToe.score
                isLost = True

    	elif move == 9:
            print 'Game Draw'
            r -= TicTacToe.score
            isDraw = True
    return s, action, r, s2, isLost, isWon, isDraw

def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc

def run():
    global discount, move, gen
    time.sleep(1)
    alpha = 1
    t = 1
    TicTacToe.setBoard()
    print 'Generation: ', gen
    while True:
        s = tuple(TicTacToe.board)
        max_act, max_val = maxQ(s)
        (s1, a, r, s2, isLost, isWon, isDraw) = do_action(max_act)

        max_act, max_val = maxQ(s2)
        inc_Q(tuple(s), a, alpha, r + discount * max_val)
        if (isLost or isWon or isDraw):
            gen += 1
            TicTacToe.reset_game('The Winner is 0')
            print 'Generation: ', gen
            move = 0
            t = 1.0
            move = 0
            time.sleep(0.01)

        t += 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)

run()
f.close()
