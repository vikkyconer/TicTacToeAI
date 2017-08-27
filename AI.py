import TicTacToe
import time
import pdb
import cPickle as pickle

discount = 0.3
actions = TicTacToe.actions
# f = open('Q.pckl', 'r')
# Q = pickle.load(f)
Q = {}
move = 0
# f.close()
# print 'initial Q: ',Q
# f = open('Q.pckl', 'w')

def maxQ(s):
    val = None
    act = None
    # print 'before: ',Q
    if (s not in Q):
        temp = {}
        for action in actions:
            temp[action] = 0.1
        Q[s] = temp
    # print 'after: ',Q
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    # print act, val
    return act, val

def do_action(action):
    global move
    s = TicTacToe.board
    r = -TicTacToe.score
    isLost = False
    isWon = False
    isDraw = False
    TicTacToe.print_board(TicTacToe.board)
    # print "Turn number " + str(move+1)
    f = 0
    if move % 2 == 0:
    	turn = 'X'
        f = TicTacToe.try_move(turn, action)
        print 'f: ',f
        if(f == -1):
            r -= TicTacToe.score
            return s, action, r, tuple(s), isLost, isWon, isDraw
            # f = TicTacToe.try_move(turn, action)
    else:
    	turn = 'O'
        # print "hello"
    	user = raw_input("Where would you like to place " + turn + " (1-9)? ")
    	user = int(user)
        f = TicTacToe.try_move(turn, user)
        while(f == -1):
            user = raw_input("Where would you like to place " + turn + " (1-9)? ")
            user = int(user)
            f = TicTacToe.try_move(turn, user)
    s2 = tuple(TicTacToe.board)
    r -= TicTacToe.score

    # Continue move and check if end of game
    move += 1
    if move > 4:
    	winner = TicTacToe.check_win(TicTacToe.board)
        # print 'winner: ', winner
    	if winner != -1:
            if winner == 1:
                print 'The winner is X'
                r += TicTacToe.score
                isWon = True
            else:
                print 'The winner is O'
                r -= TicTacToe.score
                isLost = True

    		# quit_game(board,out)
    	elif move == 9:
            print 'Game Draw'
            r -= TicTacToe.score
            isDraw = True
    return s, action, r, s2, isLost, isWon, isDraw

def inc_Q(s, a, alpha, inc):
    # print 'alpha: ', alpha
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    # pickle.dump(Q, f)

def run():
    global discount, move
    time.sleep(1)
    alpha = 1
    t = 1
    TicTacToe.setBoard()
    # pdb.set_trace()
    while True:
        # Pick the right action
        s = tuple(TicTacToe.board)
        max_act, max_val = maxQ(s)
        # print Q
        # print s
        (s1, a, r, s2, isLost, isWon, isDraw) = do_action(max_act)
        print 'reward: ',r

        # Update Q
        max_act, max_val = maxQ(s2)
        inc_Q(tuple(s), a, alpha, r + discount * max_val)
        # fil = open('Q.pckl', 'r')
        # testing = pickle.load(fil)
        # print testing
        # fil.close()
        if (isLost or isWon or isDraw):
            TicTacToe.reset_game('The Winner is 0')
            move = 0
            t = 1.0
            move = 0
            time.sleep(0.01)
            # run()
        # elif isWon:
        #     TicTacToe.reset_game('The Winner is X')
        #     print 'won'
        #     move = 0
        #     t = 1.0
        #     time.sleep(0.01)
        # elif isDraw:
        #     TicTacToe.reset_game('The Game is Draw')
        #     print 'draw'
        #     move = 0
        #     t = 1.0
        #     time.sleep(0.01)

        # Check if the game has restarted
        t += 1.0
        # if isLost:
        #     quit()
        # #     TicTacToe.restart_game()
        #     time.sleep(0.01)
            # t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)

run()
f.close()
