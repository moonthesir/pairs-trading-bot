# ⚖️ Statistical Arbitrage (Pairs Trading) Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Strategy](https://img.shields.io/badge/Strategy-Mean_Reversion-green)
![Math](https://img.shields.io/badge/Math-Cointegration-orange)

## 📌 Overview
This project implements a **Market Neutral** trading strategy based on **Statistical Arbitrage**. It identifies cointegrated pairs of assets (e.g., GOOG vs GOOGL) and executes trades based on the **Z-Score** of their spread.

Unlike trend following, this strategy relies on the mathematical probability that the "spread" between two correlated assets is stationary and will revert to the mean.

## 🧠 The Math (Cointegration)
We use the **Engle-Granger Two-Step Method**:
1.  **Hedge Ratio**: Calculated via OLS Regression: $Spread = Asset_1 - \beta \cdot Asset_2$
2.  **Stationarity**: We assume the spread follows a normal distribution over time.
3.  **Z-Score Signal**:
    $$Z = \frac{Spread - \mu}{\sigma}$$
    * **Short Signal**: $Z > 2.0$ (Spread is too wide, expect convergence)
    * **Long Signal**: $Z < -2.0$ (Spread is too narrow, expect divergence)

## 🛠️ Tech Stack
* **Statsmodels**: OLS Regression & Statistical tests
* **YFinance**: Market Data API
* **Pandas/NumPy**: Vectorized data manipulation
* **Matplotlib**: Visualization of Spread dynamics

