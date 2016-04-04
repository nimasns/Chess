import random

##########################################################

state = []
turnN = int
turnC = ''


def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation

    global turnN
    turnN = 1
    global turnC
    turnC = 'W'
    global state
    state = list('kqbnrppppp..........PPPPPNBQRK')


def chess_boardGet():
    # return the state of the game - one example is given below - note that the state has exactly 40 or 41 characters

    strOut = ''

    strOut += '1 W\n'
    strOut += 'kqbnr\n'
    strOut += 'ppppp\n'
    strOut += '.....\n'
    strOut += '.....\n'
    strOut += 'PPPPP\n'
    strOut += 'RNBQK\n'
    print strOut
    print state
    return strOut


def chess_boardSet(strIn):
    # read the state of the game from the provided argument and set your internal variables accordingly - note that the state has exactly 40 or 41 characters

    print "TESTSet"
    global state
    global turnC
    global turnN

    nc, state[0:5], state[5:10], state[10:15], state[15:20], state[20:25], state[25:30], dummy = list(strIn.split('\n'))
    turnn, turnC = nc.split(' ')
    turnN = int(turnn)
    print "STRIN"
    print strIn
    print turnN
    print turnC
    print state
    strOut = ''

    strOut += turnn
    strOut += ' '
    strOut += turnC
    strOut += '\n'
    strOut += ''.join(state[0:5]) + '\n'
    strOut += ''.join(state[5:10]) + '\n'
    strOut += ''.join(state[10:15]) + '\n'
    strOut += ''.join(state[15:20]) + '\n'
    strOut += ''.join(state[20:25]) + '\n'
    strOut += ''.join(state[25:30]) + '\n'
    print "STROUT"
    print strOut
    print "STROUT"
    return strOut


def chess_winner():
    # determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string

    return '?'


def chess_isValid(intX, intY):
    if intX < 0:
        return False

    elif intX > 4:
        return False

    if intY < 0:
        return False

    elif intY > 5:
        return False

    return True


def chess_isEnemy(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side not on move - note that we could but should not use the other is() functions in here but probably

    return False


def chess_isOwn(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably

    return False


def chess_isNothing(strPiece):
    # return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably

    return False


def chess_eval():
    # with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage

    return 0


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters

    strOut = []

    strOut.append('a5-a4\n')
    strOut.append('b5-b4\n')
    strOut.append('c5-c4\n')
    strOut.append('d5-d4\n')
    strOut.append('e5-e4\n')
    strOut.append('b6-a4\n')
    strOut.append('b6-c4\n')

    return strOut


def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here

    return []


def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here

    return []


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move

    pass


def chess_moveRandom():
    # perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here

    return 'c5-c4\n'


def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here

    return 'c5-c4\n'


def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here

    return 'c5-c4\n'


def chess_moveAlphabeta(intDepth, intDuration):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here

    return 'c5-c4\n'


def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this

    pass
