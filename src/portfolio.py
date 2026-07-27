import numpy as np
import pandas as pd

def calculate_daily_returns(prices):
    """ Calculate daily percentage return from closing prices"""
    daily_returns=prices.pct_change()
    return daily_returns

def calculate_cumulative_returns(daily_returns):
    """Calculate Cumulative Returns"""
    cumulative_returns=(1+daily_returns).cumprod()-1
    return cumulative_returns

def calculate_portfolio_returns(daily_returns,weights):
    """Calculates Expected Portfolio Return"""
    average_returns=daily_returns.mean()
    portfolio_returns=np.dot(weights,average_returns)
    return portfolio_returns

def calculate_portfolio_risk(daily_returns,weights):
    """Calculates Portfolio Volatility"""
    covariance_matrix=daily_returns.cov()
    portfolio_variance=np.dot(weights.T,np.dot(covariance_matrix,weights))
    portfolio_risk=np.sqrt(portfolio_variance)
    return portfolio_risk

def calculate_portfolio_daily_returns(daily_returns,weights):
    """Calculate daily portfolio returns."""
    portfolio_daily_returns = daily_returns.dot(weights)
    return portfolio_daily_returns

def calculate_portfolio_cumulative_returns(portfolio_daily_returns):
    """ Calculate Portfolio Cumulative Returns """
    portfolio_cumulative_returns=((1+portfolio_daily_returns).cumprod()-1)
    return portfolio_cumulative_returns

def calculate_drawdown(portfolio_daily_returns):
     """ Calculate Maximum Portfolio Drawdown """
     wealth_index=(1+portfolio_daily_returns).cumprod()
     rolling_max=wealth_index.cummax()
     drawdown=(wealth_index-rolling_max)/rolling_max
     max_drawdown=drawdown.min()
     return drawdown,max_drawdown

def calculate_sharpe_ratio(annual_portfolio_returns,annual_risk,risk_free_rate=0.06):
    """ Calculate Porfolio Sharpe Ratio """
    excess_return=(annual_portfolio_returns-risk_free_rate)
    sharpe_ratio=(excess_return/annual_risk)
    return sharpe_ratio

def calculate_cagr(portfolio_cumulative_returns):
    """ Calculate Porfolio CAGR """
    ending_value=1+portfolio_cumulative_returns.iloc[-1]
    number_of_days=len(portfolio_cumulative_returns)
    years=number_of_days/252
    cagr=((ending_value)**(1/years))-1
    return cagr

def calculate_beta(portfolio_daily_returns,benchmark_daily_returns):
    """Calculate Beta of the Portfolio"""
    covariance=portfolio_daily_returns.cov(benchmark_daily_returns)
    market_variance=benchmark_daily_returns.var()
    beta=covariance/market_variance
    return beta

def calculate_alpha(annual_portfolio_returns,annual_benchmark_return,beta,risk_free_rate=0.06):
     """Calculate portfolio alpha using CAPM."""
     market_risk_premium=(annual_benchmark_return-risk_free_rate)
     expected_return=(risk_free_rate+(market_risk_premium*beta))
     alpha=annual_portfolio_returns-expected_return
     return alpha

