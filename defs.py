import pandas as pd


def ma10(series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    moving average
    the wealth index
    """
    series['MA10'] = series['Close'].rolling(10).mean()
    series['Shares'] = [1 if series.loc[ei, 'Close'] > series.loc[ei, 'MA10'] else 0 for ei in series.index]
    series['Close1'] = series['Close'].shift(-1)
    series['Change'] = (series['Close1'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Shares'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def momentum_12_1(series: pd.Series):
     """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    momentum_12_1
    the wealth index
    """
    series['Close1'] = series['Close'].shift(12)
    series['Mom'] = (series['Close'] / series['Close1']) - 1
    series['Mom_12_1'] = [1 if series.loc[ei, 'Mom'] > 0.03 else 0 for ei in series.index]
    series['Close2'] = series['Close'].shift(-1)
    series['Change'] = (series['Close2'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Mom_12_1'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def momentum_12_2(series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    momentum_12_2
    the wealth index
    """
    series['Close1'] = series['Close'].shift(12)
    series['Close0'] = series['Close'].shift(1)
    series['Mom'] = (series['Close0'] / series['Close1']) - 1
    series['Mom_12_1'] = [1 if series.loc[ei, 'Mom'] > 0.03 else 0 for ei in series.index]
    series['Close2'] = series['Close'].shift(-1)
    series['Change'] = (series['Close2'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Mom_12_1'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    #result = (series['Wealth'] / series['Wealth'][0]) - 1
    return series['Wealth']


def avg_momentum(series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    Avg_momentum_12_6_3
    the wealth index
    """
    series['Close0'] = series['Close'].shift(12)
    series['Close1'] = series['Close'].shift(6)
    series['Close2'] = series['Close'].shift(3)
    series['Mom_0'] = ((series['Close'] / series['Close0']) - 1) * 0.33
    series['Mom_1'] = ((series['Close'] / series['Close1']) - 1) * 0.33
    series['Mom_2'] = ((series['Close'] / series['Close2']) - 1) * 0.33
    series['Avg_Mom'] = series['Mom_0'] + series['Mom_1'] + series['Mom_2']
    #series['Avg_Mom'] = sum all Mom / 3
    series['Shares'] = [1 if series.loc[ei, 'Avg_Mom'] > 0 else 0 for ei in series.index]
    series['Close2'] = series['Close'].shift(-1)
    series['Change'] = (series['Close2'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Shares'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def drawdown(series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    the previous peaks
    perecent drawdowns
    """
    wealth_index = 1000 * (1 + series['Close'].pct_change()).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return drawdowns


def low_range(series: pd.Series):
    ticker['Low'] = series['Close'].rolling(60).min() * 1.2
    #last_price = series['Close']
    series['Low_range'] = [1 if series.loc[ei, 'Close'] <= series.loc[ei, 'Low'] else 0 for ei in series.index]
    series['Close1'] = series['Close'].shift(-1)
    series['Change'] = (series['Close1'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Low_range'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def drawdown_clear(series: pd.Series):
    """
    Takes a clear times series of asset returns
    Computes and returns a DataFrame that contains:
    the previous peaks
    perecent drawdowns
    """
    wealth_index = 1000 * (1 + series.pct_change()).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return drawdowns


def trend_following(series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    trend_folloing stategy with MA and close price breakdown
    the wealth index
    """
    series['MA10'] = series['Close'].rolling(5).mean()
    series['MA5'] = series['Close'].rolling(3).mean()
    series['Close1'] = series['Close'].shift(3)
    series['Shares'] = [1 if series.loc[ei, 'MA5'] > series.loc[ei, 'MA10'] else 0 for ei in series.index]
    series['Turtle'] = [1 if series.loc[ei, 'Close'] > series.loc[ei, 'Close1'] else 0 for ei in series.index]
    series['Close2'] = series['Close'].shift(-1)
    series['Change'] = (series['Close2'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Shares'] == 1 and series.loc[ei, 'Turtle'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def cash_trigger(series: pd.Series):
    series['MA10'] = series['Close'].rolling(10).mean()
    series['Shares'] = [1 if series.loc[ei, 'Close'] > series.loc[ei, 'MA10'] else 0 for ei in series.index]
    series['Close2'] = series['CAT'].shift(-1)
    series['Change'] = (series['Close2'] - series['CAT']) / series['CAT']
    series['Profit'] = [series.loc[ei, 'Change'] if series.loc[ei, 'Shares'] == 1 else 0 for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def clear_profit(series: pd.Series):
    series['Close1'] = series['Close'].shift(-1)
    series['Change'] = (series['Close1'] - series['Close']) / series['Close']
    series['Profit'] = [series.loc[ei, 'Change'] for ei in series.index]
    series['Wealth'] = 1000 * (1 + series['Profit']).cumprod()
    return series['Wealth']


def best(ma10, mom_12_1, mom_12_2, avg_mom, tf):
    """
    Show best strategy by result
    used for test
    """
    if ma10 > mom_12_1 and ma10 > mom_12_2 and ma10 > avg_mom and ma10 > tf:
        return "ma10"
    elif mom_12_1 > ma10 and mom_12_1 > mom_12_2 and mom_12_1 > avg_mom and mom_12_1 > tf:
        return "mom_12_1"
    elif mom_12_2 > mom_12_1 and mom_12_2 > ma10 and mom_12_2 > avg_mom and mom_12_2 > tf:
        return "mom_12_2"
    elif tf > ma10 and tf > mom_12_1 and tf > mom_12_2 and tf > avg_mom:
        return "tf"
    else:
        return "avg_mom"
