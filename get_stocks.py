import yfinance as yf
import pandas as pd

print("Fetching NASDAQ data...")

# The ticker for NASDAQ-100 is ^NDX
nasdaq = yf.Ticker("^NDX")

# Get daily data for your exact 4-year Tech Winter window
hist = nasdaq.history(start="2020-01-01", end="2023-12-31")

# Clean it up to just keep Date and the Closing Price
df = hist.reset_index()
df = df[['Date', 'Close']]
df.columns = ['date', 'nasdaq_price']

# To save it
df.to_csv('nasdaq_data.csv', index=False)
print(f"Done! Saved {len(df)} days of stock data.")