import pandas as pd
import numpy as np

df = pd.read_excel(r'Data_Stocks.xlsx')

"""Use the data set and your knowledge of the first two moments computation to 
derive the optimal portfolio in the simplest case, with risk aversion parameter equal to 1, 3, 30, 100."""
# Set up weekday for weekly computation.
df['Weekday'] = [i.weekday() for i in df['Dates']]
df.set_index('Dates', inplace=True)
stocks_only = df[df.columns.difference(['Weekday'])]
# print(stocks_only.head(5))


def simple_returns(stock, period, compounded=True):
    """

    :param stock:
    :param compounded:
    :type period: object
    """
    if not compounded:
        stock_returns = stock/stock.shift(periods=period)-1
    elif compounded:
        stock_returns = np.log(stock / stock.shift(periods=period))
    stock_returns = stock_returns.iloc[period+1:, 0:-1]
    stock_returns.sort_index()
    return stock_returns


"""The different moments of our returns"""
StockReturn = simple_returns(stocks_only, 1, False)
stock_mean = StockReturn.mean()
stock_vol = StockReturn.std()
stock_skew = StockReturn.skew()
stock_kurt = StockReturn.kurtosis()
StockReturn.describe()


def mean_variance_port(means, vol):
