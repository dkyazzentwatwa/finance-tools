#####################
# SHARPE RATIO CALCULATOR #
# By David Kyazze-Ntwatwa
#####################

import numpy as np
from statistics import mean 

portfolio_return = [] #holds the set of portfolio returns to get a standard deviation.
portfolio_stddev = "" #blank variable to hold the portfolio's standard deviation.

#Calculate the Standard Deviation of a portfolio's returns
def calculate_portfolio_stddev(portfolio_return):
    portfolio_stddev = np.std(portfolio_return)
    return float(portfolio_stddev)

#Calculate the Sharpe Ratio
def calculate_sharpe_ratio(portfolio_return, risk_free_rate, portfolio_stddev):
    sharpe_ratio = (avg_port - risk_free_rate) / portfolio_stddev
    return sharpe_ratio

print("Welcome to the Sharpe Ratio Calculator! Identify a portfolio's risk easily with this calculator.")

#Enter the risk-free rate
risk_free_rate = float(input("Enter risk-free rate: (2.5-3%) "))

#Gathers a set of returns from your portfolio
while True:
    portfolio_return_ = input("Enter atleast 5 portfolio returns (or 'q' to finish): ")
    if portfolio_return_ == 'q':
        break
    portfolio_return.append(float(portfolio_return_))

avg_port = mean(portfolio_return)
print("The average portfolio return is: ", avg_port,"%")
portfolio_stddev = calculate_portfolio_stddev(portfolio_return)
print("The Standard Deviation is: ", portfolio_stddev)

sharpe_ratio = calculate_sharpe_ratio(portfolio_return, risk_free_rate, portfolio_stddev)
print(f"The Sharpe Ratio of this portfolio is: " , sharpe_ratio)

###################################