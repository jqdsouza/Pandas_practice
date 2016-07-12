# Computing Global Stats + Plotting multiple stocks

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
	
	#Return CSV file path given ticker symbol
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	
	#Read stock data (adjusted close) for given symbols from CSV files
	df = pd.DataFrame(index=dates)

	if 'SPY' not in symbols: # add SPY for reference, if absent
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
				parse_dates=True, usecols=['Date', 'Adj Close'], 
				na_values=['nan'])

		df_temp = df_temp.rename(columns={'Adj Close': symbol})

		df = df.join(df_temp)

		if symbol == 'SPY': # drop dates SPY did not trade
			df = df.dropna(subset = ["SPY"])

	return df

def plot_data(df,title="Stock prices"):

	#Plot stock prices
	ax = df.plot(title=title, fontsize=12) # ax = axis

	ax.set_xlabel("Date")
	ax.set_ylabel("Price")

	plt.show() # must be called to show plots in some environments

def test_run():

	# Read data
	dates = pd.date_range('2010-01-01', '2012-12-31')
	symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
	df = get_data(symbols, dates)
	plot_data(df)

	# Compute gloabl statistics for each stock
	print df.mean()
	print df.median()
	print df.std()

if __name__ == "__main__":
	test_run()
		