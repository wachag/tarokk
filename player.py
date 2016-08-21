# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:57:09 2016

@author: Wacha Gábor József
"""
from card import *
from trick import *
import random

class Player:
    cards=[]
    tricks=[]
    name=""
    def __init__(self):
        pass
    
    
    
    def chooseCardToTrick(self,trick):
        return random.choice(trickPossibleCards(trick,self.cards))

    def putCardToTrick(self,trick):
        choice=self.chooseCardToTrick(trick)
        self.cards.remove(choice)
        return choice

    def dump(self):
        print("-------------------")
        print(self.name)
        for t in self.tricks:
            print("Trick:")
            for c in t:
                printCard(c)