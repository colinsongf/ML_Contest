import math
import numpy as np

def med(L):
	L.sort()
	return L[len(L)/2]
def choose(x,nan):
	if x == 'NaN':
		return str(nan)
	return str(float(x))

totalData = [ [ x.strip() for x in line.split(',') ] for line in open('contest_only_test.csv') ]
median = [ med( [ float(totalData[i][j]) for i in range(len(totalData)) if totalData[i][j] != 'NaN' ] ) for j in range(len(totalData[0])) ]
completedData = [ [ choose(totalData[i][j], median[j]) for j in range(len(totalData[0])) ] for i in range(len(totalData)) ]

fp = open('completedTestDataMedian.csv','w')
for datapoint in completedData:
	fp.write(','.join(datapoint) + '\n')
fp.close()
