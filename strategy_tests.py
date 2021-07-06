lst = [
    "DIA", "IVV", "IJR", "IYR", "IWF"]

with open("index.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "ticker",
        "MA10", "MA10_Sharpe",
        "Mom_12_2", "Mom_12_2_Sharpe",
        "Mom_12_1", "Mom_12_1_Sharpe",
        "Avg_Mom", "Avg_Mom_Sharpe",
        "TF", "TF_Sharpe",
        "Clear",
    ])
    for item in lst:
        ticker = pd.read_csv(f"stocks/ETF/{item}.csv", header=0, index_col=0, parse_dates=True)

        ma10 = defs.annualized_return(defs.ma10(ticker))
        ma10_sharpe = defs.sharpe(defs.ma10(ticker))

        mom_12_2 = defs.annualized_return(defs.momentum_12_2(ticker))
        mom_12_2_sharpe = defs.sharpe(defs.momentum_12_2(ticker))

        avg_mom = defs.annualized_return(defs.avg_momentum(ticker))
        avg_mom_sharpe = defs.sharpe(defs.avg_momentum(ticker))

        mom_12_1 = defs.annualized_return(defs.momentum_12_1(ticker))
        mom_12_1_sharpe = defs.sharpe(defs.momentum_12_1(ticker))

        tf = defs.annualized_return(defs.trend_following(ticker))
        tf_sharpe = defs.sharpe(defs.trend_following(ticker))

        #best = defs.best_short(sharpe_ratio_ma10, sharpe_ratio_mom_12_2,  sharpe_ratio_avg_mom)
        clear = (defs.total_return(ticker))
        writer.writerow([
            item,
            ma10, ma10_sharpe,
            mom_12_2, mom_12_2_sharpe,
            mom_12_1, mom_12_1_sharpe,
            avg_mom, avg_mom_sharpe,
            tf, tf_sharpe,
            clear
        ])



lst = [
    "DIA", "AAPL", "AXP", "BA", "CAT", "CSCO", "CVX", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK",
    "MSFT", "NKE", "PFE", "PG", "TRV", "UNH", "V", "VZ", "WBA", "WMT", "XOM"
]

with open("faber.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "ticker", "MA10", "MA10_Sharpe",
        "Mom_12_2", "Mom_12_2_Sharpe",
        "Avg_Mom", "Avg_Mom_Sharpe",
        "TF", "TF_Sharpe",
        "Clear", "Best",
    ])
    for item in lst:
        ticker = pd.read_csv(f"stocks/DJ/{item}.csv", header=0, index_col=0, parse_dates=True)
        ma10 = defs.annualized_return(defs.ma10(ticker))
        sharpe_ratio_ma10 = defs.sharpe(defs.ma10(ticker))

        mom_12_2 = defs.annualized_return(defs.momentum_12_2(ticker))
        sharpe_ratio_mom_12_2 = defs.sharpe(defs.momentum_12_2(ticker))

        avg_mom = defs.annualized_return(defs.avg_momentum(ticker))
        sharpe_ratio_avg_mom = defs.sharpe(defs.avg_momentum(ticker))

        tf = defs.annualized_return(defs.trend_following(ticker))
        sharpe_ratio_tf = defs.sharpe(defs.trend_following(ticker))

        best = defs.best_short(sharpe_ratio_ma10, sharpe_ratio_mom_12_2,  sharpe_ratio_avg_mom)
        clear = (defs.total_return(ticker))
        writer.writerow([
            item, ma10, sharpe_ratio_ma10,
            mom_12_2, sharpe_ratio_mom_12_2,
            avg_mom, sharpe_ratio_avg_mom,
            tf, sharpe_ratio_tf,
            clear, best
        ])
