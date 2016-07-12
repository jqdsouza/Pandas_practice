#Compute daily returns

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):

	# Return CSV file path given ticker symbol
	return ospath.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):

	# Read stock data (adjusted close) for given symbols from CSV files
	df = pd.DataFrame(index=dates)

	if 'SPY' not in symbols: # add SPY for reference, if absent
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
				parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

		df_temp = df_temp.rename(columns={'Adj Close': symbol})

		df = df.join(df_temp)

		if symbol == 'SPY': # drop dates SPY did not trade
			df = df.dropna(subset=["SPY"])

	return df

def plot_data(df, title = "Stock Prices"):
	
	# Plot stock prices with a custom title and meaningful axis labels
	ax = df.plot(title = title, fontsize = 12)

	ax.set_xlabel("Date")
	ax.set_ylabel("Price")

	plt.show()

def compute_daily_returns(df):

	# Compute and return the daily return values
	# Note: Returned DataFrame must have the same number of rows

	daily_returns = df.copy() # copy given DataFrame to match size and column names

	# Compute daily returns for row 1 onwards
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1

	daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0

	# Daily returns can also be computed much more simply with the following 2 lines of code
	# daily_returns = (df / df.shift(1)) - 1 # much easier with Pandas!
	# daily_returns.ix[0, :] = 0 # Pandas leaves the 0th row full of NaNs

	return daily_returns

def test_run():

	# Read data
	dates = pd.date_range('2012-07-01', '2012-07-31') # one month only

	symbols = ['SPY','XOM']

	df = get_data(symbols, dates)

	plot_data(df)

	# Compute daily returns
	daily_returns = compute_daily_returns(df)
	plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")









