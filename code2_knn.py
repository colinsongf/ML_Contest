import numpy as np

k=10


def dist(X,Y):
	s=0
	for a,b in zip(X,Y):
		if b != 'NaN':
			s+= (a-float(b))**2
	return s**0.5

totalData = [ [ x.strip() for x in line.split(',') ] for line in open('contest_only_test.csv') ]
filledData = [[float(x) for x in line] for line in totalData if 'NaN' not in line]
missingData = [[x for x in line] for line in totalData if 'NaN' in line]
fillingData = []

while len(missingData) > 0:
	mins = [999999999]*k
	pts = [0]*k
	for line in filledData:
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

fp = open('completedTestData10NN.csv','w')
for datapoint in filledData:
	fp.write(','.join([str(x) for x in datapoint]) + '\n')
fp.close()
