# Build a dataframe in pandas

import pandas as pd

def test_run():

	#Define date range
	start_date = '2010-01-22'
	end_date = '2010-01-26'
	dates = pd.date_range(start_date,end_date)

	#Create an empty dataframe df1, with dates as index
	df1=pd.DataFrame(index=dates)
	print dates

	#print dates[0] -- geting first element of the list

	#Read SPY data into temporary dataframe
	dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",
		parse_dates=True, usecols=['Date','Adj Close'],
		na_values=['nan'])

	#print dfSPY

	#Join the two dataframes using DataFrame.join()
	df1 = df1.join(dfSPY)

	#Drop NaN Values
	df1 = df1.dropna()

	#NOTE -- lines 27 and 30 can be done in a single step, using an inner join:
	# df1.join(dfSPY,how='inner')

	print df1

if __name__ == "__main__":
	test_run()