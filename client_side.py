#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poloniex_api import poloniex
import os
import readline
import time

exit = False
polo = poloniex()

def cls():
    os.system("cls" if os.name=='nt' else "clear");

cls()

while (exit is not True):
    print("[1] Voir la balance du compte")
    print("[2] Voir les transaction en cours")
    print("[3] Voir les anciennes transactions")
    print("[4] Voir les pertes/gains")
    print("[5] Voir les toutes les transactions")
    print("[X] pour quitter le programme")
    var = input("Choix de commande: ")
    try: 
        if (var is "X" or var is "x"):
            exit = True
        elif (var is "1"):
            bal = polo.returnBalances()
            for w in bal:
                if (float(bal[w]) > 0):
                    print(w, " balance: ", bal[w])
            input()
            cls()
        elif (var is "2"):
            oo = polo.returnOpenOrders("USDT_BTC")
            for d in oo:
                print()
                for i in d:
                    print(i, ": ", d[i])
            input()
            cls()
        elif (var is "3"):
            print(polo.returnTradeHistory("all"))
            input()
            cls()
        elif (var is "4"):
            dw = polo.returnDepositsWithdrawals(0, time.time())
            for i in dw:
                print(i)
                for e in dw[i]:
                    for y in e:
                        print("\t", y, ": ", e[y])
            input()
            cls()
        else:
            print(var)
            input()
            cls()
    except (ValueError, NameError) as e:
        print("ERROR: ", e)
        input()
        cls()
