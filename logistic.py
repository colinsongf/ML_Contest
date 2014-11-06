import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score
from sklearn.lda import LDA
from sklearn.preprocessing import normalize
import score

data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])


normdata = normalize(data[:,:-1])
prj = LDA(n_components = 100)

# clf = LogisticRegression()
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle = True)
output =[]
finalscore = 0
counter = 0
for train, test in skf:
	counter = counter + 1
	newdata = prj.fit_transform([ normdata[i][:] for i in train ],[ data[i][-1] for i in train ])
	newtestdata = prj.transform([ normdata[i][:] for i in test ])
	clf = LogisticRegression(class_weight='auto')
	clf = clf.fit(newdata, [ data[i][-1] for i in train ])
	prediction = clf.predict( newtestdata)
	finalscore = finalscore + score.get_score( prediction ,[ data[i][-1] for i in test ])
# score = cross_val_score(clf, normdata[:,:], data[:,-1], cv = 5, scoring = 'f1')
# print "out of score"
# for i in score:
# 	print i

finalscore = finalscore *(1.0)/counter
print finalscore