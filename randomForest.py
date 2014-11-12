import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score
from sklearn.preprocessing import normalize
import score


data = np.array([ [ float(x) for x in line.split(',') ] for line in open('completedData10NN.csv') ])
normdata = normalize(data[:,:-1])
print "data done"
print "logistic initialized"
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle = True)
output =[]
counter = 0
finalscore = 0
print "getting in"
flad = [0.99]*700 + [0.01]*2800
for train, test in skf:
	counter = counter + 1
	clf = RandomForestClassifier(n_estimators = 1000, n_jobs = 8 , max_features = 0.1)
	clf = clf.fit([ normdata[i][:] for i in train ], [ data[i][-1] for i in train ])
	prediction = clf.predict([ normdata[i][:] for i in test ])
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	xscore = score.get_score(prediction, [ data[i][-1] for i in test ])
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