ticker = pd.read_csv("stocks/CAT.csv", header=0, index_col=0, parse_dates=True)
cat = ticker["Close"]
returns = cat.pct_change()
returns = returns.dropna()

returns.std()
annualized_vol = returns.std() * np.sqrt(12)
total_return = (returns + 1).prod() - 1

n_months = returns.shape[0]
return_per_month = ((returns + 1).prod() ** (1 / n_months) - 1).round(3)
annualized_return = (returns + 1).prod() ** (12 / n_months) - 1

riskfree_rate = 0.03
excess_return = annualized_return - riskfree_rate
sharpe_ratio = (excess_return / annualized_vol).round(3)
sharpe_ratio_ma10 = defs.sharpe(defs.ma10(ticker))


test["Mom_12_2_Sharpe"][2:].mean()

d = pd.read_csv("stocks/DJ/dual_sample.csv", header=0, index_col=0, parse_dates=True, sep=';')

defs.drawdown(ticker).min()


plt.rcParams["figure.figsize"] = [10, 5]
ticker["Close"].plot(label="Close", legend=True)
trend = ticker["Close"].rolling(10).mean().plot(label="MA10", legend=True)

plt.figure(figsize=(10, 8))

defs.ma10(ticker).plot()
defs.avg_momentum(ticker).plot()
defs.momentum_12_2(ticker).plot()
plt.show()

index_ = pd.read_csv("stocks/ETF/GEM/IVV.csv", header=0, index_col=0)
t_bill = pd.read_csv("stocks/ETF/GEM/SHV.csv", header=0, index_col=0)
index_close = index_["Close"]
bill_close = t_bill["Close"]

new = pd.concat([index_close, bill_close], axis=1)
new.columns = ["SP500", "T-bills"]
