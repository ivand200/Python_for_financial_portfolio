import requests
#import sys
import json
import click




class Ep:

    def shares_outstanding(ticker):
        """Get shares outstanding"""
        try:
            url = requests.get(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=defaultKeyStatistics").json()
            return (url["quoteSummary"]["result"][0]["defaultKeyStatistics"]["sharesOutstanding"]["raw"])
        except:
            return 0

    def average_income(ticker):
        """Average income for last 4 years"""
        try:
            url = requests.get(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=incomeStatementHistory").json()
            year1 = (url["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][0]["netIncome"]["raw"])
            year2 = (url["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][1]["netIncome"]["raw"])
            year3 = (url["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][2]["netIncome"]["raw"])
            year4 = (url["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][3]["netIncome"]["raw"])
        except:
            return 0
        else:
            return (year1 + year2 + year3 + year4) / 4


    def get_ep(self, ticker):
        """E/P"""
        try:
            e_p = (Ep.average_income(ticker) / Ep.shares_outstanding(ticker))
        except:
            return 0
        else:
            return e_p


class Stock:

    def __init__(self, ticker):
        self.ticker = ticker
        self._ep = Ep()

    def close(self):
        url = f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{self.ticker}?modules=price"
        data = requests.get(url).json()
        close_price = data["quoteSummary"]["result"][0]["price"]["regularMarketPreviousClose"]["raw"]
        return close_price

    def ep(self):
        e = self._ep.get_ep(self.ticker)
        return e


@click.command()
@click.option('--stock', help='ticker')
@click.option('--task', prompt='Enter method(ep, close)',  help='ep, close')

def _main(stock, task):
    stock_ = Stock(str(stock))
    if task == "ep":
        earnings = stock_.ep()
        print(earnings)
    elif task == "close":
        last_close = stock_.close()
        print(last_close)



if __name__ == "__main__":
    _main()
