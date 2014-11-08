import math
import numpy as np

def med(L):
	L.sort()
	return L[len(L)/2]
def choose(x,nan):
	if x == 'NaN':
		return nan
	return float(x)

totalData = np.array([ [ x.strip() for x in line.split(',') ] for line in open('ML-contest-training/contest_train.csv') ])
median = ( [ med( [ float(totalData[i][j]) for i in range(len(totalData)) if (totalData[i][j] != 'NaN' and int(totalData[i][-1]) == 1) ] ) for j in range(len(totalData[0])-1) ], [ med( [ float(totalData[i][j]) for i in range(len(totalData)) if (totalData[i][j] != 'NaN' and int(totalData[i][-1]) == 2) ] ) for j in range(len(totalData[0])-1) ] )
# mean = ( [ avg( [ float(totalData[i][j]) for i in range(len(totalData)) if (totalData[i][j] != 'NaN' and int(totalData[i][-1]) == 1) ] ) for j in range(len(totalData[0])-1) ], [ avg( [ float(totalData[i][j]) for i in range(len(totalData)) if (totalData[i][j] != 'NaN' and int(totalData[i][-1]) == 2) ] ) for j in range(len(totalData[0])-1) ] )
median[0].append(1)
median[1].append(2)
completedData = np.array([ [ choose(totalData[i][j], median[int(totalData[i][-1])-1][j]) for j in range(len(totalData[0])) ] for i in range(len(totalData)) ])

features = completedData[:, :-1]
labels = completedData[:, -1]
class1 = np.array([ datapoint[:-1] for datapoint in completedData if datapoint[-1] == 1 ])
class2 = np.array([ datapoint[:-1] for datapoint in completedData if datapoint[-1] == 2 ])

fp = open('completedDataMedian.csv','w')
for row in class1:
	for x in row:
		fp.write(str(x) + ',')
	fp.write('1\n')
for row in class2:
	for x in row:
		fp.write(str(x) + ',')
	fp.write('2\n')
fp.close()
