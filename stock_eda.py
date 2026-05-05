# ============================================================
#  Stock Market Exploratory Data Analysis
#  Author : Ruhani Narang
#  GitHub : github.com/narang-arch
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("tab10")

# ============================================================
#  1. GENERATE SAMPLE DATA  
# ============================================================
np.random.seed(42)

stocks = {
    'RELIANCE': 2400, 'TCS': 3500, 'INFY': 1500,
    'HDFCBANK': 1600, 'WIPRO': 450,  'TATAMOTORS': 600,
    'SBIN':     550,  'ADANIENT': 2200, 'ONGC': 180,
    'BAJFINANCE': 6500
}

dates = pd.date_range(start='2019-01-01', end='2023-12-31', freq='B')

price_data = {}
for ticker, start_price in stocks.items():
    returns   = np.random.normal(0.0003, 0.015, len(dates))
    prices    = start_price * np.cumprod(1 + returns)
    price_data[ticker] = prices

df = pd.DataFrame(price_data, index=dates)
df.index.name = 'Date'

print("=" * 60)
print("  STOCK MARKET EDA — Ruhani Narang")
print("=" * 60)
print(f"\nDataset: {len(df)} trading days | {len(stocks)} stocks")
print(f"Period : {df.index[0].date()} to {df.index[-1].date()}")
print("\nFirst 5 rows:")
print(df.head())

# ============================================================
#  2. DATA QUALITY CHECK
# ============================================================
print("\n── Data Quality ──────────────────────────────────────")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"\nData types:\n{df.dtypes}")

# ============================================================
#  3. FEATURE ENGINEERING
# ============================================================
# Daily returns
returns_df = df.pct_change().dropna()
returns_df.columns = [c + '_ret' for c in df.columns]

# Moving averages for RELIANCE
df['REL_MA30']  = df['RELIANCE'].rolling(30).mean()
df['REL_MA90']  = df['RELIANCE'].rolling(90).mean()

# Rolling volatility (30-day std of returns)
df['REL_VOL30'] = returns_df['RELIANCE_ret'].rolling(30).std() * np.sqrt(252)

# Annualised return & risk for each stock
annual_returns = returns_df[[c for c in returns_df.columns]].mean() * 252
annual_risk    = returns_df[[c for c in returns_df.columns]].std()  * np.sqrt(252)
annual_returns.index = [c.replace('_ret','') for c in annual_returns.index]
annual_risk.index    = [c.replace('_ret','') for c in annual_risk.index]

print("\n── Annualised Return & Risk ──────────────────────────")
summary = pd.DataFrame({
    'Annual Return (%)' : (annual_returns * 100).round(2),
    'Annual Risk (Std)' : annual_risk.round(4)
})
print(summary)

# ============================================================
#  4. VISUALISATIONS
# ============================================================
fig = plt.figure(figsize=(20, 24))
fig.suptitle("Stock Market Exploratory Data Analysis\nRuhani Narang | github.com/narang-arch",
             fontsize=16, fontweight='bold', y=0.98)

# ── Plot 1: Normalised Price Trends ─────────────────────────
ax1 = fig.add_subplot(4, 2, 1)
norm = df[list(stocks.keys())].div(df[list(stocks.keys())].iloc[0]) * 100
for col in norm.columns:
    ax1.plot(norm.index, norm[col], label=col, linewidth=1.2)
ax1.set_title("Normalised Price Trends (Base=100)", fontweight='bold')
ax1.set_ylabel("Indexed Price")
ax1.legend(fontsize=6, ncol=2)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# ── Plot 2: Moving Averages (RELIANCE) ──────────────────────
ax2 = fig.add_subplot(4, 2, 2)
ax2.plot(df.index, df['RELIANCE'],  label='RELIANCE', alpha=0.6, linewidth=1)
ax2.plot(df.index, df['REL_MA30'], label='30-Day MA', linewidth=1.5)
ax2.plot(df.index, df['REL_MA90'], label='90-Day MA', linewidth=1.5)
ax2.set_title("RELIANCE — Price & Moving Averages", fontweight='bold')
ax2.set_ylabel("Price (₹)")
ax2.legend()
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# ── Plot 3: Daily Returns Distribution ──────────────────────
ax3 = fig.add_subplot(4, 2, 3)
for col in ['RELIANCE_ret','TCS_ret','INFY_ret']:
    sns.kdeplot(returns_df[col], ax=ax3, label=col.replace('_ret',''), linewidth=1.5)
ax3.axvline(0, color='red', linestyle='--', linewidth=1)
ax3.set_title("Daily Returns Distribution", fontweight='bold')
ax3.set_xlabel("Daily Return")
ax3.legend()

# ── Plot 4: Rolling Volatility ───────────────────────────────
ax4 = fig.add_subplot(4, 2, 4)
ax4.plot(df.index, df['REL_VOL30'], color='crimson', linewidth=1.2)
ax4.fill_between(df.index, df['REL_VOL30'], alpha=0.2, color='crimson')
ax4.set_title("RELIANCE — 30-Day Rolling Volatility (Annualised)", fontweight='bold')
ax4.set_ylabel("Volatility")
ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# ── Plot 5: Correlation Heatmap ──────────────────────────────
ax5 = fig.add_subplot(4, 2, 5)
corr = returns_df.corr()
corr.index   = [c.replace('_ret','') for c in corr.index]
corr.columns = [c.replace('_ret','') for c in corr.columns]
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, ax=ax5, mask=mask, annot=True, fmt=".2f",
            cmap='RdYlGn', center=0, linewidths=0.5,
            annot_kws={"size": 7})
ax5.set_title("Return Correlation Heatmap", fontweight='bold')
ax5.tick_params(axis='x', rotation=45, labelsize=7)
ax5.tick_params(axis='y', rotation=0,  labelsize=7)

# ── Plot 6: Risk vs Return ───────────────────────────────────
ax6 = fig.add_subplot(4, 2, 6)
colors = plt.cm.tab10(np.linspace(0, 1, len(annual_returns)))
for i, (ticker, ret) in enumerate(annual_returns.items()):
    risk = annual_risk[ticker]
    ax6.scatter(risk, ret, s=120, color=colors[i], zorder=5)
    ax6.annotate(ticker, (risk, ret),
                 textcoords="offset points", xytext=(5, 4),
                 fontsize=7)
ax6.axhline(0, color='gray', linestyle='--', linewidth=0.8)
ax6.set_xlabel("Annual Risk (Std Dev)")
ax6.set_ylabel("Annual Return")
ax6.set_title("Risk vs. Return — All Stocks", fontweight='bold')

# ── Plot 7: Yearly Average Return by Stock ───────────────────
ax7 = fig.add_subplot(4, 2, 7)
avg_ret = (annual_returns * 100).sort_values()
colors_bar = ['#d73027' if v < 0 else '#1a9850' for v in avg_ret]
ax7.barh(avg_ret.index, avg_ret.values, color=colors_bar)
ax7.axvline(0, color='black', linewidth=0.8)
ax7.set_title("Annualised Return by Stock (%)", fontweight='bold')
ax7.set_xlabel("Return (%)")

# ── Plot 8: Box Plot of Daily Returns ────────────────────────
ax8 = fig.add_subplot(4, 2, 8)
plot_df = returns_df.copy()
plot_df.columns = [c.replace('_ret','') for c in plot_df.columns]
plot_df.boxplot(ax=ax8, vert=True, patch_artist=True,
                boxprops=dict(facecolor='#74add1', color='navy'),
                medianprops=dict(color='red', linewidth=2))
ax8.set_title("Distribution of Daily Returns (Box Plot)", fontweight='bold')
ax8.set_ylabel("Daily Return")
ax8.tick_params(axis='x', rotation=45, labelsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("stock_market_eda_plots.png", dpi=150, bbox_inches='tight')
print("\n✅ Plot saved as stock_market_eda_plots.png")
plt.show()

# ============================================================
#  5. SUMMARY STATISTICS
# ============================================================
print("\n── Descriptive Statistics (Daily Returns) ────────────")
desc = returns_df.describe().T
desc.index = [c.replace('_ret','') for c in desc.index]
desc['skewness'] = returns_df.skew().values
desc['kurtosis'] = returns_df.kurtosis().values
print(desc[['mean','std','min','max','skewness','kurtosis']].round(4))

print("\n Analysis complete!")

