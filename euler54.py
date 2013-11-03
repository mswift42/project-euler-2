#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Poker hands
Problem 54
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
2C 3S 8S 8D TD
Pair of Eights
Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
2C 5C 7D 8S QH
Highest card Queen
Player 1
3	 	2D 9C AS AH AC
Three Aces
3D 6D 7D TD QD
Flush with Diamonds
Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
3D 6D 7H QD QS
Pair of Queens
Highest card Seven
Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
3C 3D 3S 9S 9D
Full House
with Three Threes
Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?"""

hands = []

import operator
from collections import defaultdict

card_rank = ['2' , '3' , '4' , '5', '6', '7', '8', '9' , 'T', 'J' , 'Q', 'K', 'A']
card_dic = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12 }


with open('poker.txt', 'r+') as f:
    for i in f.readlines():
        hands.append(i.split())

def royal_flush(hand):
    set_kind = {i[0] for i in hand}
    set_suit = {i[1] for i in hand}
    return len(set_suit) == 1 and sorted(set_kind) == ['A','J','K','Q','T']

def strait_flush(hand):
    set_kind = {i[0] for i in hand}
    set_suit = {i[1] for i in hand}
    rank = sorted([card_dic[i] for i in set_kind])
    return len(set_suit)==1 and rank[4] - rank[0] == 4 

def sort_hand(hand):
    card_dic = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12 }
    valuelist = list(((card_dic[i[0]],i) for i in hand))
    return sorted(valuelist, reverse=True)


def get_sets(hand):
    set_kind = {i[0] for i in hand}
    set_suit = {i[1] for i in hand}
    return set_kind, set_suit

def four_kind(hand):
    set_kind, set_suit = get_sets(hand)
    return len(set_suit) == 4 and len(set_kind) == 2 
    
def full_house(hand):
    set_kind, set_suit = get_sets(hand)
    return len(set_kind) == 2 and len(set_suit) >=3

def flush(hand):
    set_kind, set_suit = get_sets(hand)
    return len(set_suit) == 1

def straight(hand):
    set_kind, set_suit = get_sets(hand)
    rank = sorted([card_dic[i] for i in set_kind])
    return len(set_kind) == 5 and rank[4] - rank[0] == 4


def three_kind(hand):
    set_kind, set_suit = get_sets(hand)
    handlist = [i[0] for i in hand]
    return len(set_kind) == 3 and 3 in [handlist.count(i) for i in handlist]

def two_pair(hand):
    set_kind, set_suit = get_sets(hand)
    handlist = [i[0]  for i in hand]
    return len(set_kind) == 3 and [handlist.count(i) for i in handlist].count(2) ==4 

def one_pair(hand):
    set_kind, set_suit = get_sets(hand)
    handlist = [i[0] for i in hand]
    return [handlist.count(i) for i in handlist].count(2)==2 

def high_card(hand):
    "return high card"
    handlist = sort_hand(hand)
    return handlist[0]


def get_score(hand):
    if royal_flush(hand): return 10
    elif strait_flush(hand): return 9
    elif four_kind(hand): return 8
    elif full_house(hand): return 7
    elif flush(hand): return 6
    elif straight(hand): return 5
    elif three_kind(hand): return 4
    elif two_pair(hand): return 3
    elif one_pair(hand): return 2
    else:
        return 1


count1 = 0
count2 = 0

ties = []


for i in hands:
    if get_score(i[:5]) > get_score(i[5:]):
        count1 +=1
    elif get_score(i[:5]) < get_score(i[5:]):
        count2 +=1


else:
    ties.append(i)



onepairlist = []
highlist = []

for i in ties:
    if get_score(i[:5]) ==2:
        onepairlist.append(i)
    elif get_score(i[:5]) ==1:
        highlist.append(i)

for i in highlist:
    if sort_hand(i[:5]) > sort_hand(i[5:]):
        count1 +=1
    elif sort_hand(i[:5]) < sort_hand(i[5:]):
        count2 +=1 


for i in onepairlist:
    hand1 = [j[0] for j in i[:5]]
    hand2 = [j[0] for j in i[5:]]
    pair1 = [i for i in hand1 if hand1.count(i)==2 ]
    pair2 = [i for i in hand2 if hand2.count(i)==2 ]
    if card_dic[pair1[0]] > card_dic[pair2[0]]:
        count1 +=1
    elif card_dic[pair1[0]] < card_dic[pair2[0]]:
        count2 +=1
    else:
        for i in pair1:
            if i in hand1:
                hand1.remove(i)
        for i in pair2:
            if i in hand2:
                hand2.remove(i)
        if sort_hand(hand1) > sort_hand(hand2):
            count1 +=1
        else:
            count2 +=1 

print(count1)






