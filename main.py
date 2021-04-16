import yfinance as yf
import pandas as pd
# import numpy as np
import finviz
import json

class Portfolio:
    def __init__(self, name):
        self.name = name

        self.stocks = {}
    
    def addStocks(self, ticker, amountOwned):
        self.stocks[ticker] = amountOwned

    # TODO: Write finviz get price function
    def getPrice(self, ticker):
        return finviz.get_stock(ticker)

    def calculateEarnings(self, dict):
        print("================")
        for key, value in dict.items():
            result = yf.Ticker(key)
            # price = result.history(start="2021-03-04", end="2021-03-08")
            result = result.dividends
            df = pd.DataFrame(data=result)
            try: 
                singleDiv = df.iloc[df.size-1].Dividends
            except:
                singleDiv = 0
            compute = singleDiv * 4
            computeyear = compute * value

            finvizResults = self.getPrice(key)

            print("Lastest Dividend Amount from "+str(key)+ ": $"+str(singleDiv))
            print("Annual Predicted Dividend Income from "+str(key)+ ": $"+str(computeyear))
            print("Lastest Close Price: "+str(finvizResults['Price']))
            print("================")


