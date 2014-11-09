import numpy as np


k=10


def dist(X,Y):
	s=0
	for a,b in zip(X,Y):
		if b != 'NaN':
			s+= (a-float(b))**2
	return s**0.5

totalData = [ [ x.strip() for x in line.split(',') ] for line in open('ML-contest-training/contest_train.csv') ]
filledData = [[float(x) for x in line] for line in totalData if 'NaN' not in line]
missingData = [[x for x in line] for line in totalData if 'NaN' in line]
fillingData = []

while len(missingData) > 0:
	mins = [999999999]*k
	pts = [0]*k
	for line in filledData:
		if line[-1] != float(missingData[0][-1]):
			continue
		x=dist(line,missingData[0])
		y=mins.index(max(mins))
		if x < mins[y]:
			mins[y] = x
			pts[y]=line
	while (missingData[0].count('NaN') > 0):
		p=missingData[0].index('NaN')
		missingData[0][p] = sum([pt[p] for pt in pts])/k
	fillingData.append([float(x) for x in missingData[0]])
	missingData = missingData[1:]

filledData.extend(fillingData)

class1 = [ datapoint[:-1] for datapoint in filledData if datapoint[-1] == 1 ]
class2 = [ datapoint[:-1] for datapoint in filledData if datapoint[-1] == 2 ]

fp = open('completedData10NN.csv','w')
for row in class1:
	for x in row:
		fp.write(str(x) + ',')
	fp.write('1\n')
for row in class2:
	for x in row:
		fp.write(str(x) + ',')
	fp.write('2\n')
fp.close()
