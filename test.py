import csv
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import defs


#index = pd.read_csv("stocks/DIA.csv", header=0, index_col=0, parse_dates=True)
#ticker = pd.read_csv("stocks/CVX.csv", usecols = ["Close"])

lst = [
    "DIA", "AAPL", "AXP", "BA", "CAT", "CSCO", "CVX", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK",
    "MSFT", "NKE", "PFE", "PG", "TRV", "UNH", "V", "VZ", "WBA", "WMT", "XOM"
]

with open("sample2.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ticker", "MA10", "Mom_12_1", "Mom_12_2", "Avg_Mom", "TF", "Best", "Clear", "MD"])
    for item in lst:
        ticker = pd.read_csv(f"stocks/DJ/{item}.csv", header=0, index_col=0, parse_dates=True)
        ma10 = round((defs.ma10(ticker)[-2] / 1000) - 1, 2)
        #ma10_md = round(defs.drawdown2(defs.ma10(ticker)).min(), 2)
        mom_12_1 = round((defs.momentum_12_1(ticker)[-2] / 1000) - 1, 2)
        #mom_12_1_md = round(defs.drawdown2(defs.momentum_12_1(ticker)).min(), 2)
        mom_12_2 = round((defs.momentum_12_2(ticker)[-2] / 1000) - 1, 2)
        #mom_12_2_md = round(defs.drawdown2(defs.momentum_12_2(ticker)).min(), 2)
        avg_mom = round((defs.avg_momentum(ticker)[-2] / 1000) - 1, 2)
        #avg_mom_md = round(defs.drawdown2(defs.avg_momentum(ticker)).min(), 2)
        tf = round((defs.trend_following(ticker)[-2] / 1000) - 1, 2)
        #tf_md = round(defs.drawdown2(defs.trend_following(ticker)).min(), 2)
        best = defs.best(ma10, mom_12_1, mom_12_2, avg_mom, tf)
        MD = round(defs.drawdown(ticker).min(), 2)
        clear = round((defs.clear_profit(ticker)[-2] / 1000) -1, 2)
        writer.writerow([item, ma10, mom_12_1, mom_12_2, avg_mom, tf, best, clear, MD])


#s2 = pd.read_csv("sample2.csv", header=0, index_col=0, parse_dates=True)
#s2["Avg_Mom"][2:].mean()
#s2["Mom_12_2"][2:].mean()
#s2["MA10"][2:].mean()
#x =  round(defs.drawdown2(defs.avg_momentum(index)).min(), 2)
