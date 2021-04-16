from main import Portfolio
import finviz
import json

portfolio1 = Portfolio("StockFund")
portfolio1.addStocks('TSLA', 4)
portfolio1.addStocks('CAT', 1)
print(str(portfolio1.name))
portfolio1.calculateEarnings(portfolio1.stocks)

finvizResults = str(finviz.get_analyst_price_targets('CAT')[0]['date'])+ ", Firm: " + str(finviz.get_analyst_price_targets('CAT')[0]['analyst'])+ ", Rating: " + str(finviz.get_analyst_price_targets('CAT')[0]['rating'])

print(finvizResults)
#print(finvizResults['Price'])