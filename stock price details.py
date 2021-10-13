import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd
ticker = []
Number_of_stocks = int(input("Enter number of stocks"))
for i in range(Number_of_stocks):
    Stock_name = input("Enter stock name which is mentioned in yahoo finance ")
    ticker.append(Stock_name)
    data = YahooFinancials(ticker)
data.get_open_price()
data.get_summary_data()
df = pd.DataFrame()
df
tickers = ['HDFC']
for ticker in tickers:
    data = YahooFinancials(ticker)
    open_price = data.get_open_price()
    currency = data.get_currency()
    yearly_high = data.get_yearly_high()

    new_row = {
        "ticker": ticker,
        "open_price": open_price,
        "currency": currency,
        "yearly_high": yearly_high,
    }

    df = df.append(new_row, ignore_index=True)
    df
