import numpy as np

#Downloads Market Data from Yahoo Finance
from src.data_loader import download_stock_data
tickers=["HDFCBANK.NS","TCS.NS","INFY.NS"]
prices=download_stock_data(tickers)
benchmark_prices=download_stock_data(["^NSEI"])



from src.portfolio import (calculate_daily_returns,
calculate_cumulative_returns,calculate_portfolio_returns,
calculate_portfolio_risk,calculate_portfolio_daily_returns,
calculate_portfolio_cumulative_returns,calculate_drawdown,
calculate_sharpe_ratio,calculate_cagr,calculate_beta,
calculate_alpha)

#Computes daily return of the Individual Stocks in Portfolio and of Benchmark
returns=calculate_daily_returns(prices)
benchmark_returns=calculate_daily_returns(benchmark_prices)

benchmark_daily_returns = benchmark_returns["^NSEI"] #as the benchamark_return was a DataFrame while the daily_returns is a series hecne we converted the same
average_benchmark_return=benchmark_daily_returns.mean()
annual_benchmark_return=average_benchmark_return*252#Annual Benchmark Return

#Computation of Cumulative Daily Return of Individual Stock and Benchmark
cumulative_returns=calculate_cumulative_returns(returns)
benchmark_cumulative_returns=calculate_cumulative_returns(benchmark_returns)

#Computation of Portfolio returns and Portfolio Annual Return based on the weights of each stock
weights=np.array([0.4,0.35,0.25]) #Put the weight of the Stock here
portfolio_returns=calculate_portfolio_returns(returns,weights)
portfolio_daily_returns=calculate_portfolio_daily_returns(returns,weights)
portfolio_cumulative_returns=calculate_portfolio_cumulative_returns(portfolio_daily_returns)
annual_portfolio_returns=portfolio_returns*252

#Computation of Portfolio Risk
portfolio_risk=calculate_portfolio_risk(returns,weights)
annual_risk=portfolio_risk*np.sqrt(252)

#Computation of Drawdown, Sharpe Ratio, CAGR, Beta and Alpha of the Portfolio Simultaneously
drawdown,maxdrawdown=calculate_drawdown(portfolio_daily_returns)
sharpe_ratio=calculate_sharpe_ratio(annual_portfolio_returns,annual_risk)
cagr=calculate_cagr(portfolio_cumulative_returns)
beta=calculate_beta(portfolio_daily_returns,benchmark_daily_returns)
alpha=calculate_alpha(annual_portfolio_returns,annual_benchmark_return,beta)


from src.visualization import (plot_portfolio_growth,
plot_correlation_heatmap,plot_portfolio_allocation,
plot_stock_performance,plot_portfolio_drawdown,plot_portfolio_vs_benchmark)

plot_portfolio_growth(portfolio_cumulative_returns)

plot_correlation_heatmap(returns)

plot_portfolio_allocation(weights,tickers)

plot_stock_performance(cumulative_returns)

plot_portfolio_drawdown(portfolio_cumulative_returns)

plot_portfolio_vs_benchmark(portfolio_cumulative_returns,benchmark_cumulative_returns)

from src.report_generator import (generate_excel_report)

generate_excel_report(annual_portfolio_returns,annual_risk,tickers,sharpe_ratio,cagr,beta,alpha)


print("="*50)
print("      PORTFOLIO PERFORMANCE SUMMARY")
print("="*50)
print(f"Annual Return      : {annual_portfolio_returns:.2%}")
print(f"Annual Risk        : {annual_risk:.2%}")
print(f"Maximum Drawdown   : {maxdrawdown:.2%}")
print( f"Sharpe Ratio       : {sharpe_ratio:.2f}")
print(f"Portfolio CAGR    : {cagr:.2%}")
print(f"Annual Benchmark Return(NIFTY 50)      : {annual_benchmark_return:.2%}")
print(f"Portfolio Beta     : {beta:.2f}")
print(f"Portfolio Alpha    : {alpha:.2%}")







