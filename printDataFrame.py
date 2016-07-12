import pandas as pd

def test_run():
	df = pd.read_csv("data/AAPL.csv")
	print df #print entire dataframe

	#print df.head() -- prints first 5 rows of data
	#print df.tail() -- prints last 5 rows of data

	#print df[10:21] -- prints rows of data between index 10 and 20 
	#                -- slicing operation

if __name__ == "__main__":
	test_run()

