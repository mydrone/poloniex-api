#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poloniex_api import poloniex
import os
import readline
import time

exit = False
polo = poloniex()

def cls():
    input()
    os.system("cls" if os.name=='nt' else "clear");

while (exit is not True):
    print("[1] Voir la balance du compte")
    print("[2] Voir les transaction en cours")
    print("[3] Voir les anciennes transactions")
    print("[4] Voir les pertes/gains")
    print("[5] Voir toutes les transactions")
    print("[6] Acheter")
    print("[7] Vendre")
    print("[8] Annuler une commande")
    print("[X] pour quitter le programme")
    var = input("Choix de commande: ")
    try:
#-----------------ON EXIT-----------------
        if (var is "X" or var is "x"):
            exit = True
#------------ON SHOW BALANCE--------------
        elif (var is "1"):
            bal = polo.returnBalances()
            for w in bal:
                if (float(bal[w]) > 0):
                    print(w, " balance: ", bal[w])
            cls()
#------------ON SHOW OPEN ORDERS----------
        elif (var is "2"):
            oo = polo.returnOpenOrders("USDT_BTC")
            for d in oo:
                print()
                for i in d:
                    print(i, ": ", d[i])
            cls()
#-----------ON SHOW TRADE HISTORY---------
        elif (var is "3"):
            print(polo.returnTradeHistory("all"))
            cls()
#------------ON SHOW GAINS/LOSSES---------
        elif (var is "4"):
            dw = polo.returnDepositsWithdrawals(0, time.time())
            for i in dw:
                print(i)
                for e in dw[i]:
                    for y in e:
                        print("\t", y, ": ", e[y])
            cls()
#------------ON SHOW MARKET HISTORY-------
        elif (var is "5"):
            tradeHistory = polo.returnMarketTradeHistory('USDT_BTC')
            for som in tradeHistory:
                print("------------------------------")
                for indiv in som:
                    print(indiv, ":", som[indiv])
            cls()
#-----------------ON BUY------------------
        elif (var is "6"):
            print("----------ACHETER----------")
            buyRate = input("Entrez le prix d'achat (US): ")
            buyAmount = input("Entrez la quantité à acheter (BTC): ")
            buyConfirm = input("Confirmer la commande d'achat de " + buyAmount + " Bitcoin au prix de " + buyRate + "$USD (y/n): ")
            if (buyConfirm is "y"):
                print("Achat en cours...")
                print("Votre code d'achat est le: ", polo.buy("USDT_BTC", float(buyRate), float(buyAmount)))
            else:
                print("Welp RIP")
            cls()
#-----------------ON SELL-----------------
        elif (var is "7"):
            print("----------VENDRE----------")
            sellRate = input("Entrez le prix de vente (US): ")
            sellAmount = input("Entrez la quantité à acheter (BTC): ")
            sellConfirm = input("Confirmer la commande de vente de " + sellAmount + " Bitcoin au prix de " + sellRate + "$USD (y/n): ")
            if (sellConfirm is "y"):
                print("Vente en cours...")
                print("Votre code de vente est le: ", polo.sell("USDT_BTC", float(sellRate), float(sellAmount)))
            else:
                print("Welp RIP")
            cls()
#----------------ON CANCEL----------------
        elif (var is "8"):
            print("----------ANNULER----------")
            cancelNb = input("Entrez le numéro de commande: ")
            cancelConfirm = input("Ètes-vous sûr de vouloir annuler la commande " + cancelNb + "? (y/n): ")
            if (sellConfirm is "y"):
                print("Annulation en cours...")
                if (polo.cancel(int(cancelNb) is 1)):
                    print("Commande annulée avec succès!")
                else:
                    print("Welp didn't work, good luck with that")
            else:
                print("Welp RIP")
            cls()
#-------------ON ANYTHING ELSE------------
        else:
            print(var)
            input()
            cls()
    except (ValueError, NameError, Exception) as e:
        print("ERROR: ", e)
        cls()
        pass
