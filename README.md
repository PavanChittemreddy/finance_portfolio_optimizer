# Stock Volatility & Portfolio Optimizer

A comprehensive case study demonstrating volatility analysis, covariance exploration, and efficient-frontier simulation using Python, Plotly, and Streamlit.

🚀 Live Demo

[View the Streamlit App](https://financeportfoliooptimizer-but3xfztguhfwfd8yn6ltb.streamlit.app/)

🔧 Installation & Local Run

Clone the repo

git clone https://github.com/PavanChittemreddy/finance_portfolio_optimizer
cd finance-portfolio-optimizer

Set up your environment

python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\activate.ps1
# macOS/Linux:
source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run notebooks

jupyter lab notebooks/fetch_and_visualize.ipynb
jupyter lab notebooks/volatility_and_cov.ipynb

Launch Streamlit demo

streamlit run dashboard/app.py

✨ Methodology

Data Fetch: Pull 1 year of daily closing prices for AAPL, MSFT, GOOGL, AMZN, TSLA using yfinance.

Exploration: Visualize time-series lines and compute a correlation heat-map.

Volatility: Calculate annualized volatility and plot a bar chart.

Covariance: Compute annualized covariance matrix and display as a heat-map.

Simulation: Monte Carlo simulate 2,000 random portfolios to plot the efficient frontier.

Interactive Demo: Build a Streamlit app for dynamic ticker selection and live visualization.

🎯 Key Outputs

heatmap.png: Correlation Matrix of Daily Returns

volatility_pct.png: Annualized Volatility by Ticker (%)

covariance.png: Annualized Covariance Matrix

efficient_frontier.png: Simulated Portfolios & Efficient Frontier

📦 Requirements

Listed in requirements.txt:

pandas
numpy
yfinance
plotly
streamlit

📄 License

This project is released under the MIT License. Feel free to clone and adapt for your own portfolio.
