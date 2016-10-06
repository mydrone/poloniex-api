import urllib, urllib.request
import json
import time
import hmac,hashlib
from .models import ApiCredentials
from .poloniex_api import poloniex

class server:
    def __init__(self):
        self.polo = poloniex()
    
    def credentials_checker(self, request):
        keyReceived = request.META.get('HTTP_KEY')
        signReceived = request.META.get('HTTP_SIGN')
        req = {}
        req['command'] = request.POST['command']
        req['nonce'] = int(request.POST['nonce'])
        try:
            apiCredentials = ApiCredentials.objects.filter(key=keyReceived)[0]
            signInDb = hmac.new(bytearray(apiCredentials.secret, 'ascii'), bytearray(urllib.parse.urlencode(req), 'ascii'), hashlib.sha512).hexdigest()
            if signReceived == signInDb:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def dispatcher_public(self, request):
        dicti = request.GET
        command = dicti['command']
        if command == 'returnTradeHistory':
            return self.return_market_trade_history(dicti['currencyPair'])
        return {}

    def dispatcher_trading(self, request):
        if not self.credentials_checker(request):
            return { 'Error' : 'Invalid credentials' }
        dicti = request.POST
        command = dicti['command']
        if command == 'returnBalances':
            return self.return_balances()
        elif command == 'returnOpenOrders':
            return self.return_open_orders(dicti['currencyPair'])
        elif command == 'returnTradeHistory':
            return self.return_trade_history(dicti['currencyPair'])
        elif command == 'returnDepositsWithdrawals':
            return self.return_deposits_withdrawals(dicti['start'], dicti['end'])
        elif command == 'buy':
            return self.buy(dicti['currencyPair'], dicti['amount'], dicti['rate'])
        elif command == 'sell':
            return self.sell(dicti['currencyPair'], dicti['amount'], dicti['rate'])
        return {}

    def return_ticker(self):
        #Business Logic
        return self.polo.returnTicker()

    def return_24_volume(self):
        #Business Logic        
        return self.polo.return24Volume()
    
    def return_order_book(self, currencyPair):
        #Business Logic        
        return self.polo.returnOrderBook()

    def return_market_trade_history(self, currencyPair):
        #Business Logic        
        return self.polo.returnMarketTradeHistory(currencyPair)
    
    def return_balances(self):
        #Business Logic        
        return self.polo.returnBalances()
    
    def return_open_orders(self, currencyPair):
        #Business Logic        
        return self.polo.returnOpenOrders(currencyPair)

    def return_trade_history(self, currencyPair):
        #Business Logic        
        return self.polo.returnTradeHistory(currencyPair)
    
    def buy(self, currencyPair, rate, amount):
        #Business Logic        
        return self.polo.buy(currencyPair, rate, amount)

    def sell(self, currencyPair, rate, amount):
        #Business Logic        
        return self.polo.sell(currencyPair, rate, amount)

    def cancel(self, currencyPair, orderNumber):
        #Business Logic        
        return self.polo.cancel(currencyPair, orderNumber)

    def withdraw(self, currency, amount, address):
        #Business Logic        
        return self.polo.withdraw(currency, amount, address)
    
    def generate_new_address(self, currency):
        #Business Logic        
        return self.polo.generateNewAddress(currency)
    
    def return_deposits_withdrawals(self, start, end):
        #Business Logic        
        return self.polo.returnDepositsWithdrawls(start, end)