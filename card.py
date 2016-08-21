# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:04:48 2016

@author: Wacha Gábor József
"""

def suit(card):
    if(card>=20): 
        return 4
    return int(card/5)

def rank(card):
    if(suit(card)<4):
        return card%5
    return card-19

def strongerCard(card1,card2):
    if(suit(card1)==suit(card2)):
        if (rank(card1)>rank(card2)):
            return card1
        return card2
    if(suit(card2)==suit(42)):
        return card2
    return card1


def printCard(card):
    suits=['PIKK','KOR','KARO','TREFF','TAROKK','TAROKK','TAROKK','TAROKK','TAROKK']
    ranks=['ASZ','BOTOS','LOVAS','DAMA','KIRALY']
    cSuit=suit(card)
    cRank=rank(card)
    if(cSuit<4):
      print( suits[cSuit],ranks[cRank])
    else:
      print (suits[cSuit],cRank)
