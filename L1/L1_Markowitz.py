import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import minimize


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
StockReturn = pd.DataFrame(simple_returns(stocks_only, 1, False))
stock_mean = pd.DataFrame(StockReturn.mean())
stock_vol = pd.DataFrame(StockReturn.std())
stock_skew = pd.DataFrame(StockReturn.skew())
stock_kurt = pd.DataFrame(StockReturn.kurtosis())
stock_vcv = StockReturn.cov()
StockReturn.describe()


# def obj_without_rf():


# Initial guess of portfolio weight, setting it to equally weighted for now
def initial_weight(assets):
    init = []
    n = len(assets)
    for i in range(n):
        init.append(1/n)
    return init


# Deriving the mean variance portfolio depending on whether
# we are including risk-free assets.
# def mean_var_port(means, vcv, rf_asset=False):
#     if not rf_asset:
#         init_weight = pd.DataFrame(initial_weight(means))
#         objective = 1/2 * init_weight.transpose() * stock_vcv * init_weight
#         constraint1 = means.transpose() * init_weight - means.transpose() * ini
