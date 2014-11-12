from sklearn.neighbors import KNeighborsClassifier
# neigh = KNeighborsClassifier(n_neighbors=11)
# neigh.fit(trainData, 600*[0]+600*[1])
# pred = neigh.predict(testData)

import numpy as np
from sklearn.preprocessing import normalize
from sklearn.cross_validation import cross_val_score, StratifiedKFold
import score

data = np.array([ [ float(x) for x in line.split(',') ] for line in open('completedData10NN.csv') ])

normdata = normalize(data[:,:-1])
newdata = normdata
print len(newdata)
print len(newdata[0])
print np.shape(newdata)
print "data done"
print "logistic initialized"
print "fitted data"
skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle=True)
output =[]
finalscore = 0
counter = 0

for train, test in skf:
	counter = counter + 1	
	neigh = KNeighborsClassifier(n_neighbors=120)
	neigh.fit([ newdata[i][:] for i in train ], [ data[i][-1] for i in train ])
	prediction = neigh.predict([ newdata[i][:] for i in test ])
	xscore = score.get_score( prediction , [ data[i][-1] for i in test ])
	finalscore = finalscore + xscore
	print xscore
	print "done"
finalscore = finalscore * (1.0) / counter
print counter
print finalscore
