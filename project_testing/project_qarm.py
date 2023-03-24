import numpy as np
import pandas as pd


market_cap = pd.read_excel('Group_G copy.xlsx', sheet_name=1)
price_index = pd.read_excel('Group_G copy.xlsx', sheet_name=2, index_col='Date')
revenue = pd.read_excel('Group_G copy.xlsx', sheet_name=3)
emission = pd.read_excel('Group_G copy.xlsx', sheet_name=4)


def assets_returns(assets, period, compounded=True):
    if not compounded:
        asset_return = (assets / assets.shift(periods=period)) - 1
    elif compounded:
        asset_return = np.log(assets / assets.shift(periods=period))

    # asset_return.drop(index=asset_return.index[0:abs(period)], axis=0, inplace=True)
    return asset_return


if __name__ == '__main__':
    simple_return = assets_returns(price_index.loc[:, price_index.columns != 'Date'], period=1, compounded=False)
    print(simple_return)