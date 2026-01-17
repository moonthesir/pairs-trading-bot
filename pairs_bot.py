import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# --- 1. CONFIGURATION ---
asset1 = 'GOOG'
asset2 = 'GOOGL'
start = '2023-01-01'
end = '2024-01-01'

# --- 2. FETCH DATA ---
print(f"📥 Fetching data for {asset1} and {asset2}...")
# FIX: Download both together to ensure aligned Index
data = yf.download([asset1, asset2], start=start, end=end)['Close']

# --- 3. ALIGN DATA ---
df = pd.DataFrame()
df['Asset1'] = data[asset1]
df['Asset2'] = data[asset2]
df.dropna(inplace=True)

# --- 4. CALCULATE HEDGE RATIO ---
# OLS Regression to find the perfect ratio
x = sm.add_constant(df['Asset2'])
model = sm.OLS(df['Asset1'], x).fit()
hedge_ratio = model.params.iloc[1]
print(f"Hedge Ratio: {hedge_ratio:.4f}")

# Calculate the Spread
df['Spread'] = df['Asset1'] - (hedge_ratio * df['Asset2'])

# --- 5. Z-SCORE (The Signal) ---
window = 30
df['Mean'] = df['Spread'].rolling(window=window).mean()
df['Std'] = df['Spread'].rolling(window=window).std()
df['Z_Score'] = (df['Spread'] - df['Mean']) / df['Std']

# --- 6. VISUALIZE ---
plt.figure(figsize=(12, 8))

# Plot 1: The Spread (The Rubber Band)
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Spread'], label='Spread')
plt.axhline(df['Spread'].mean(), color='black', alpha=0.5, linestyle='--')
plt.title(f'The Spread: {asset1} - ({hedge_ratio:.2f} * {asset2})')
plt.legend()

# Plot 2: Z-Score (The Trading Signals)
plt.subplot(2, 1, 2)
plt.plot(df.index, df['Z_Score'], label='Z-Score', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axhline(2.0, color='red', linestyle='--', label='Short Signal (+2)')
plt.axhline(-2.0, color='green', linestyle='--', label='Long Signal (-2)')
plt.title('Z-Score (Mean Reversion Signals)')
plt.legend()

plt.tight_layout()
plt.show()
