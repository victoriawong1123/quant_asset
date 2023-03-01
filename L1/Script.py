# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:17:52 2021

@author: Florian IELPO
"""

# Setting the right working folder
#
# import os
#
# os.chdir("//fileserver2//PersonalFolders$//fie//My Documents//Perso//HEC//")
#
# print("Current working directory: {0}".format(os.getcwd()))
#
#
#
#

# import data

import pandas as pd

filename = "Data_Stocks.xlsx";

xls = pd.ExcelFile(filename)

Returns_Dates = pd.read_excel(xls, 'Sheet1')

#
#
# Label


# Formating dates

import numpy as np

date_list = Returns_Dates.Dates;

datesFormated = pd.to_datetime(date_list, format="%d.%m.%Y");

EquityPrices = Returns_Dates.iloc[:, 1:11];  # Excluding the S&P500

num_lines = np.size(EquityPrices, 0);

simpleReturns = np.divide(EquityPrices.iloc[2:(num_lines), :], EquityPrices.iloc[1:(num_lines - 1), :]) - 1

Expectation = np.mean(simpleReturns, 0)

Sigma = np.cov(np.transpose(simpleReturns));

Sigma_inv = np.linalg.inv(Sigma);

Sigma_inv = pd.DataFrame(Sigma_inv);

Expectation = pd.DataFrame(Expectation);

Expectation = np.transpose(Expectation);

optimal_weight = np.matmul(Expectation, Sigma_inv);

optimal_weight = np.array(optimal_weight);

# Plots

import matplotlib.pyplot as plt

labels = list(EquityPrices);

plt.figure(dpi=120)

plt.bar(labels, optimal_weight[0])

plt.xticks(rotation=90)

plt.title('Optimal Allocation')

# Why these returns?

labels = list(EquityPrices);

plt.figure(dpi=120)

plt.bar(labels, Expectation.iloc[0] * 52)

plt.xticks(rotation=90)

plt.title('Average returns')

plt.bar(labels, np.power(np.diag(Sigma), 0.5) * np.power(52, .5))

plt.xticks(rotation=90)

plt.title('Volatility')

# What happens now when changing the time period considered?
