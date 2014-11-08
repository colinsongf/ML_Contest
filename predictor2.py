import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import normalize

clf = GradientBoostingClassifier(warm_start = True, n_estimators=1500)
print 'clf created'

trainData = np.array([ [ float(x.strip()) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])
train = normalize(trainData[:,:-1])
print 'train data read'

clf.fit(train, trainData[:,-1])
print 'clf trained'

testData = [ [ float(x.strip()) for x in line.split(',') ] for line in open('completedTestData.csv') ]
newdata = normalize(testData)
print np.shape(newdata)
print "test data read"

prediction = clf.predict(newdata)
print "predicted"

f = open('team04.txt', 'w')
def num(x):
	if x == 1:
		return 'A'
	elif x == 2:
		return 'B'
	else:
		print 'error' + str(x)+type(x)
		return 'B'
for i in prediction:
	f.write(num(i)+'\n')
print 'wrote to file'

f.close()
print 'done'
