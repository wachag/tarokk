# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:00:56 2016

@author: Wacha Gábor József
"""
from functools import reduce
import random
from player import Player
from card import *        

names=["Oki","Attila","Tamás","Berci"]    
     
deck=list(range(0,42))

random.shuffle(deck)
p=list()
for i in range(0,4):
    pl=Player()
    pl.name=names[i]
    pl.cards=deck[i*9:(i+1)*9]
    pl.tricks=[]
    p.append(pl)

for x in p:
    x.cards.sort()

starter=random.randrange(0,4)

for i in range(0,9):
    trick=list()
    for player in range(starter,starter+4):
        print(p[player%4].name)      
        choice=p[player%4].putCardToTrick(trick)
        trick.append(choice)
        printCard(choice)
    winnerCard=reduce(strongerCard,trick)
    print("Winner:")
    printCard(winnerCard)
    starter=int(deck.index(winnerCard)/9)
    p[starter].tricks.append(trick)
    print("Next starter",p[starter].name)
    print("")

for pl in p:
    print(pl.name, len(pl.tricks))
