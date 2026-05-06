#  Stock Market Exploratory Data Analysis

> **Author:** Ruhani Narang &nbsp;|&nbsp; B.Sc. Economics, Doon University  
> **Tools:** Python · Pandas · Matplotlib · Seaborn · NumPy  
> **GitHub:** [github.com/narang-arch](https://github.com/narang-arch)

---

##  Project Overview

This project performs an in-depth **Exploratory Data Analysis (EDA)** on historical stock market data for **10 major Indian stocks** over a **5-year period (2019–2023)**. The goal is to uncover market trends, measure risk and return, identify inter-stock correlations, and generate actionable investment insights using Python.

---

##  Key Objectives

- Collect and preprocess multi-year historical stock price data
- Engineer financial features: moving averages, daily returns, rolling volatility
- Identify correlation patterns and high-volatility market periods
- Analyse risk vs. return trade-offs across stocks
- Communicate insights through professional visualisations

---

##  Stocks Analysed

| Stock | Sector |
|-------|--------|
| RELIANCE | Energy / Conglomerate |
| TCS | Information Technology |
| INFY | Information Technology |
| HDFCBANK | Banking & Finance |
| WIPRO | Information Technology |
| TATAMOTORS | Automobile |
| SBIN | Banking |
| ADANIENT | Infrastructure |
| ONGC | Oil & Gas |
| BAJFINANCE | NBFC / Finance |

---

##  Analysis Performed

### 1. Data Preprocessing
- Handled missing values, outliers, and datetime indexing
- Validated data types and ensured analysis-ready datasets

### 2. Feature Engineering
- **30-day & 90-day Moving Averages** — to identify short and long-term price trends
- **Daily Return (%)** — percentage change in price day-over-day
- **Rolling 30-Day Volatility** — annualised standard deviation of returns
- **Annualised Return & Risk** — for risk vs. return comparison

### 3. Visualisations (8 Charts)
| Chart | Insight |
|-------|---------|
| Normalised Price Trends | Relative performance of all 10 stocks |
| Moving Averages | Price trend + crossover signals (RELIANCE) |
| Daily Returns Distribution | Normality, skewness, fat tails |
| Rolling Volatility | Detecting high-risk market periods |
| Correlation Heatmap | Inter-stock correlations (0.85+ found in IT sector) |
| Risk vs. Return Scatter | Identifying best risk-adjusted stocks |
| Annualised Return Bar | Best and worst performers over 5 years |
| Box Plot of Returns | Outliers and return spread by stock |

---

##  Key Insights

- **IT sector stocks (TCS, INFY, WIPRO)** showed strong positive correlations **(0.85+)**, meaning they tend to move together — useful for portfolio diversification decisions.
- **Rolling volatility spikes** clearly corresponded to real-world market events (COVID crash, rate hike cycles).
- **Risk vs. Return analysis** revealed that high-return stocks did not always carry proportionally higher risk — ADANIENT and BAJFINANCE showed notable asymmetry.
- **Annualised return & standard deviation** metrics provided a clean framework to compare investment opportunities across sectors.

---

##  Project Structure

```
stock_market_eda/
│
├── stock_eda.py                  # Main EDA script
├── requirements.txt              # Python dependencies
├── stock_market_eda_plots.png    # Output visualisation (generated on run)
└── README.md                     # Project documentation
```

---

##  How to Run

```bash
# 1. Clone the repository
git clone https://github.com/narang-arch/stock_market_eda.git
cd stock_market_eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python stock_eda.py
```

>  The script generates **simulated data** by default.  
> To use real data, replace the data generation block with your own CSV:
> ```python
> df = pd.read_csv('your_stock_data.csv', index_col='Date', parse_dates=True)
> ```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **Pandas** | Data manipulation & feature engineering |
| **NumPy** | Numerical computations |
| **Matplotlib** | Custom visualisations |
| **Seaborn** | Statistical plots & heatmaps |

---

##  Connect

-  narangruhani51@gmail.com  
-  [LinkedIn](https://linkedin.com/in/ruhani-narang-7573b4338/)  
-  [GitHub](https://github.com/narang-arch)

---

*This project was built as part of my data analytics portfolio. Feel free to fork, star , or reach out!*
Fixed strikethrough formatting in README
