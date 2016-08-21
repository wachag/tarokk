# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:20:33 2016

@author: Wacha Gábor József
"""

from card import *

def trickPossibleCards(trick, hand):
    if(len(trick)==0):
        return hand
    f=list(filter(lambda card: suit(trick[0])==suit(card),hand))
    if(len(f)==0):
        f=list(filter(lambda card: suit(42)==suit(card),hand))
    if(len(f)==0):
        f=hand
    return f