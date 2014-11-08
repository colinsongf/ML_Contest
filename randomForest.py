import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score


data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])
print "data done"
print "logistic initialized"
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
skf = StratifiedKFold(data[:,-1], n_folds=5, shuffle = True)
output =[]
counter = 0
finalscore = 0
print "getting in"
for train, test in skf:
	counter = counter + 1
	clf = RandomForestClassifier(n_estimators = 500, n_jobs = 8 , bootstrap = False)
	clf = clf.fit([ data[i][:-1] for i in train ], [ data[i][-1] for i in train ])
	prediction = clf.predict([ data[i][:-1] for i in test ])
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	xscore = f1_score([ data[i][-1] for i in test ], prediction)
	output.append(xscore)
	print xscore
	print "done"
# score = cross_val_score(clf, data[:,:-1], data[:,-1], cv = 5, scoring = 'f1')
print "out of score"
for i in output:
	print i
	finalscore = finalscore + i

finalscore = finalscore*(1.0)/counter

print finalscore