import yfinance as yf
import matplotlib.pyplot as plt 
import seaborn as sns 

nifty = yf.Ticker("^NSEI")
df = nifty.history(period="60d")

# 1. Grab the last 30 rows and immediately reset the index
nifty_30_days_close = df[['Close']].tail(30).reset_index()

# Now 'Date' exists as a normal column!
print(nifty_30_days_close)

# 2. Convert Date to a cleaner string format so the x-axis labels read nicely
nifty_30_days_close['Date'] = nifty_30_days_close['Date'].dt.strftime('%m-%d')
sns.lineplot(x='Date', y='Close', data=nifty_30_days_close)
plt.xlabel("Dates")
plt.ylabel("Close")
plt.title("NIFTY last 30 days performance")

# 3. Pass the formatted string dates directly for the ticks
plt.xticks(rotation=90)
plt.tight_layout()  # Prevents the x-labels from getting clipped at the bottom
plt.show()