# given a list of hands, how many times does player 1 win?
# standard 5-card poker,  ranking as follows (highest to lowest):
# Royal Flush:      Ace, King, Queen, Jack, Ten, same suit
# Straight Flush:   Consecutive cards, same suit
# Four-of-a-kind:   Four cards of the same value
# Full house:       Three-of-a-kind and a Pair
# Flush:            All cards the same suit
# Straight:         Five consecutive cards (different suits)
# Three-of-a-kind:  Three cards of the same value
# Two Pairs:        Two different Pairs
# Pair:             Two cards of the same value
# High Card:        Highest Value Card
from collections import Counter

face_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

rank_values = {'HC':0, 'PR':1, 'TP':2, '3K':3, 'ST':4, 'FL':5, 'FH':6, '4K':7, 'SF':8, 'RF': 9}

def get_hand(cards):
    faces = [card[0] for card in cards]
    suits = set([card[1] for card in cards])
    return (faces, suits)

def is_straight(faces):
    vals = sorted([face_values[face] for face in faces])
    for i in xrange(len(vals)-1):
        if vals[i+1] != vals[i]+1:
            return False
    else:
        return True

def is_flush(suits):
    return len(suits) == 1

def get_rank(hand):
    #is it a flush?
    if is_flush(hand[1]):
        if sorted(hand[0]) == sorted('AKQJT'):
            #it's a royal flush
            return 'RF'
        elif is_straight(hand[0]):
            #its a straight flush
            return 'SF'
        else:
            #it's just a flush
            return 'FL'
    elif is_straight(hand[0]):
        # it's a straight
        return 'ST'
    else:
        #it's a four of a kind, full house, three of a kind, two pair, pair, or high card
        rank = Counter(hand[0])
        if len(rank.keys()) == 2:
            #its a four of a kind or a full house
            if max(rank.values()) == 4:
                return '4K'
            else:
                return 'FH'
        elif len(rank.keys()) == 3:
            #it's a three of a kind or two pairs
            if max(rank.values()) == 3:
                return '3K'
            else:
                return 'TP'
        elif len(rank.keys()) == 4:
            #it's a pair
            return 'PR'
        else:
            #we're down to High card
            return 'HC'

def get_winner(hand1, hand2):
    rank1 = rank_values[get_rank(hand1)]
    rank2 = rank_values[get_rank(hand2)]
    if rank1 > rank2:
        #player 1 wins by rank
        return 1
    elif rank2 > rank1:
        #player 2 wins by rank
        return 2
    else:
        #players have equal rank, settle it by the highest card
        cards1 = Counter([face_values[face] for face in hand1[0]])
        cards2 = Counter([face_values[face] for face in hand2[0]])
        ranked1 = [tup[0] for i in range(4,0,-1) for tup in sorted(cards1.items(),reverse=True) if tup[1] == i]
        ranked2 = [tup[0] for i in range(4,0,-1) for tup in sorted(cards2.items(),reverse=True) if tup[1] == i]
        if ranked1 > ranked2:
            return 1
        elif ranked2 > ranked1:
            return 2
        else:
            return -1


with open('prob54hands') as f_hands:

    hands = [hand.strip().split() for hand in f_hands]

player1wins = 0
player2wins = 0
unknowns = 0
for hand in hands:
    hand1 = get_hand(hand[:5])
    hand2 = get_hand(hand[5:])
    winner = get_winner(hand1,hand2)
    if winner == 2:
        player2wins += 1
    elif winner == 1:
        player1wins += 1
    else:
        unknowns += 1

print "Player 1 won {} hands, Player 2 won {} hands, program couldn't tell the difference {} times".format(player1wins, player2wins, unknowns)
