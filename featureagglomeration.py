import numpy as np
from sklearn.cross_validation import cross_val_score, StratifiedKFold
import score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cluster
data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])

alg = cluster.FeatureAgglomeration(n_components = 1897, n_clusters = 200)
alg.fit(data[:,:-1])
newdata = alg.transform(data[:,:-1])
print np.shape(newdata)

skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle=True)
output =[]
finalscore = 0
counter = 0

for train, test in skf:
	counter = counter + 1	
	clf = GradientBoostingClassifier(warm_start = True, n_estimators = 1000 , learning_rate = 0.05)
	clf = clf.fit([ newdata[i][:] for i in train ], [ data[i][-1] for i in train ])
	prediction = clf.predict([ newdata[i][:] for i in test ])
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	xscore = score.get_score( prediction , [ data[i][-1] for i in test ])
	finalscore = finalscore + xscore
	print xscore
	print "done"
finalscore = finalscore * (1.0) / counter
print counter
print finalscore
