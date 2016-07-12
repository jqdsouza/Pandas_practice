# Plotting multiple stocks

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

	# Define a date range
	dates = pd.date_range('2010-01-01' '2010-12-31') # the year 2010

	# Choose stock symbols to read
	symbols = ['GOOG', 'IBM', 'GLD'] # SPY will be added in get_data()

	#Get stock data
	df = get_data(symbols, dates)

	#print df

	#Slice by row range (dates) using DataFrame.ix[] selector
	# print df.ix['2010-01-01':'2010-01-31'] # the month of January

	#Slice by column (symbols)
	# print df['GOOG'] # a single label selects a single column
	# print df[['IBM', 'GLD']] # a list of labels selects multiple columns

	# Slice by row and column
	print df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']]