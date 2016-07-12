#Utility functions

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):

	#Return CSV file path given ticker symbol
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	
	#Read stock data (adjusted close) for given symbols from CSV files
	df = pd.DataFrame(index=dates)

	if 'SPY' not in symbols: #add SPY for reference, if absent
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		
		#Read data for each symbol
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
								parse_dates=True, usecols=['Date','Adj Close']
								, na_values=['nan'])

		#rename to prevent clash
		df_temp = df_temp.rename(columns={'Adj Close': symbol})

		#join data for each symbol
		df = df.join(df_temp) # use default how='left'

		#drop dates SPY did not trade
		if symbol == 'SPY':
			df = df.dropna(subset=["SPY"])

	return df

