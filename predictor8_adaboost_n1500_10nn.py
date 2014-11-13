from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.svm import SVC
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score, make_scorer
import score

clf = AdaBoostClassifier(n_estimators = 1500)
print 'clf created'

trainData = np.array([ [ float(x.strip()) for x in line.split(',') ] for line in open('completedData10NN.csv') ])
train = normalize(trainData[:,:-1])
print 'train data read'

# clf.fit(train, trainData[:,-1])
flad = np.array([0.8]*700 + [0.2]*2800)

clf.fit(train, trainData[:,-1],flad)
print 'clf trained'

testData = [ [ float(x.strip()) for x in line.split(',') ] for line in open('completedTestData10NN.csv') ]
newdata = normalize(testData)
print np.shape(newdata)
print "test data read"

prediction = clf.predict(newdata)
print "predicted"

f = open('team04_adaboost_n1500_10NN_result.txt', 'w')
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

