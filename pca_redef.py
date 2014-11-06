from sklearn.decomposition import PCA
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score, make_scorer
import score

data = [ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ]

# data = []
# data.extend(xdata[0:700])
# data.extend(xdata[0:700])
# data.extend(xdata[0:700])
# data.extend(xdata)
data = np.array(data)
normdata = normalize(data[:,:-1])


print len(normdata)

labels = data[:,-1]

print np.shape(normdata)


print "data done"
print "logistic initialized"
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
skf = StratifiedKFold(labels, n_folds=5, shuffle=True)
# output =[]
for train, test in skf:
	trainL=[]
	labels2=[]
	testL=[]
	labels3=[]
	for i in train:
		trainL.append(i)
		labels2.append(labels[i])
		if labels[i]==1:
			trainL.append(i)
			trainL.append(i)
			trainL.append(i)
			labels2.append(1)
			labels2.append(1)
			labels2.append(1)
	for i in test:
		testL.append(i)
		labels3.append(labels[i])
		if labels[i]==1:
			testL.append(i)
			testL.append(i)
			testL.append(i)
			labels3.append(1)
			labels3.append(1)
			labels3.append(1)

	prj = PCA(n_components = 10)
	newdata = prj.fit_transform([normdata[i][:] for i in trainL ], labels2)#[ labels[i] for i in trainL ])
	newtestdata = prj.transform([normdata[i][:] for i in testL ])
	print np.shape(newdata)
	clf = RandomForestClassifier(n_estimators = 500)
	clf = clf.fit(newdata, labels2)
	prediction = clf.predict(newtestdata)
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	print score.get_score(prediction, labels3) #[ labels[i] for i in test ])
print "done"
# score = cross_val_score(clf, newdata[:,:], data[:,-1], cv = 5, scoring = 'get_score')
# print "in scores"
# for i in score:
# 	print i

# print "out of score"
# for i in output:
# 	print i
