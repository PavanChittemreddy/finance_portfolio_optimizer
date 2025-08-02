# dashboard/app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ── 1. Load & clean data ──
@st.cache_data
def load_data():
    df = pd.read_csv("../data/close_prices.csv", index_col="Date", parse_dates=True)
    df = df.bfill().ffill().dropna()
    returns = df.pct_change().dropna()
    return df, returns

df, returns = load_data()
mean_ret = returns.mean() * 252
cov_mat  = returns.cov()  * 252

# ── 2. UI: title & ticker selector ──
st.title("📊 Portfolio Volatility & Efficient Frontier")
tickers = st.multiselect(
    "Select tickers to include",
    options=df.columns.tolist(),
    default=df.columns.tolist()
)

if len(tickers) < 2:
    st.warning("Please select at least two tickers.")
    st.stop()

subset = returns[tickers]

# ── 3. Volatility bar chart ──
vol = subset.std() * np.sqrt(252) * 100
fig_vol = px.bar(
    x=vol.index, y=vol.values,
    labels={"x":"Ticker", "y":"Annual Volatility (%)"},
    title="Annualized Volatility by Ticker (%)"
)
fig_vol.update_yaxes(range=[0, vol.max()*1.1])
st.subheader("🔍 Annualized Volatility")
st.plotly_chart(fig_vol, use_container_width=True)

# ── 4. Efficient frontier ──
mean_sel = subset.mean() * 252
cov_sel  = subset.cov()  * 252

n_sims = 2000
results = np.zeros((3, n_sims))
for i in range(n_sims):
    w = np.random.random(len(tickers))
    w /= w.sum()
    port_ret = np.dot(w, mean_sel)
    port_vol = np.sqrt(w.T @ cov_sel @ w)
    results[0,i] = port_vol
    results[1,i] = port_ret
    results[2,i] = port_ret / port_vol

port_df = pd.DataFrame(results.T, columns=["vol","ret","sharpe"])

fig_eff = px.scatter(
    port_df,
    x="vol", y="ret",
    color="sharpe",
    labels={"vol":"Volatility","ret":"Expected Return","sharpe":"Sharpe Ratio"},
    title="Efficient Frontier (simulated portfolios)"
)
st.subheader("🚀 Efficient Frontier")
st.plotly_chart(fig_eff, use_container_width=True)

# ── 5. Footer/link ──
st.markdown("---")
st.markdown(
    "See the full code on [GitHub](https://github.com/YourUserName/finance-portfolio-optimizer)."
)
