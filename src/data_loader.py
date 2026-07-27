import os
import pandas as pd
import yfinance as yf

def download_stock_data(tickers,period="1y"):
    """
    Download Historical Prices from Yahoo Finance.
    Paramters:
    tickers:List of stock tickers
    period=Time period(default=1y)
    Returns:
    pandas.DataFrame"""
    data=yf.download(tickers=tickers,period=period,auto_adjust=False,progress=False)
    if data.empty:
        raise ValueError("No Data Downloaded!,Please Check the Ticker:)")
    close_prices=data["Close"]
    os.makedirs("data/raw",exist_ok=True)
    close_prices.to_csv("data/raw/my_prices.csv")
    return close_prices
