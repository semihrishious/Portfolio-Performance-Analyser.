import os
import matplotlib.pyplot as plt
import seaborn as sns

def plot_portfolio_growth(portfolio_cumulative_returns):
    """Plot Cumulative Portfolio Growth"""
    os.makedirs("charts",exist_ok=True)
    plt.figure(figsize=(10,6))
    plt.plot(portfolio_cumulative_returns)
    plt.title("Portfolio Growth")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.savefig("charts/portfolio_growth.png")
    plt.show()

def plot_correlation_heatmap(daily_returns):
    """Plot Correlation matrix as a heatmap"""
    correlation_matrix=daily_returns.corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(correlation_matrix,annot=True,cmap="RdYlGn",linewidth=0.5)
    plt.title("Correlation Heatmap")
    os.makedirs("charts",exist_ok=True)
    plt.savefig("charts/correlation_heatmap.png")
    plt.show()

def plot_portfolio_allocation(weights,tickers):
    """Plot Portfolio Allocation"""
    plt.figure(figsize=(8,8))
    plt.pie(weights,labels=tickers,autopct="%1.1f%%",
    startangle=90,shadow=True)
    plt.axis("equal")
    plt.title("Portfolio Allocation")
    os.makedirs("charts",exist_ok=True)
    plt.savefig("charts/portfolio_allocation.png")
    plt.show()

def plot_stock_performance(cumulative_returns):
    """Plot Cumulative Returns of each stock"""
    plt.figure(figsize=(12,6))
    plt.plot(cumulative_returns)
    plt.legend(cumulative_returns.columns)
    plt.title(" Individual Stock Performance")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.savefig("charts/stock_performance.png")
    plt.show()

def plot_portfolio_drawdown(drawdown):
    """Plot Portfolio Drawdown"""
    os.makedirs("charts",exist_ok=True)
    plt.figure(figsize=(10,6))
    plt.plot(drawdown)
    plt.title("Portfolio Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.savefig("charts/portfolio_drawdown.png")
    plt.show()

def plot_portfolio_vs_benchmark(portfolio_cumulative_returns,benchmark_cumulative_returns):
    """Plot Returns of Portfolio and Benchmark for Comparison"""
    plt.figure(figsize=(12,6))
    plt.plot(portfolio_cumulative_returns.index,portfolio_cumulative_returns,label="Portfolio")
    plt.plot(benchmark_cumulative_returns.index,benchmark_cumulative_returns,label="Benchmark")
    plt.legend()
    plt.title("Portfolio vs Benchmark Growth")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.savefig("charts/portfoliovsbenchmark.png")
    plt.show()
    