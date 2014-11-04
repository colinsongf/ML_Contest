import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score

data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])
print "data done"
# print "logistic initialized"
# # clf.fit(data[:,:-1], data[:,-1])
# print "fitted data"
# skf = StratifiedKFold(data[:,-1], n_folds=5)
# output =[]
# for train, test in skf:
# 	clf = LogisticRegression(class_weight='auto' )
# 	clf = clf.fit([ data[i][:-1] for i in train ], [ data[i][-1] for i in train ])
# 	prediction = clf.predict([ data[i][:-1] for i in test ])
# 	output.append(f1_score([ data[i][-1] for i in test ], prediction))
score = cross_val_score(clf, data[:,:-1], data[:,-1], cv = 5, scoring = 'f1')
print "out of score"
for i in output:
	print i