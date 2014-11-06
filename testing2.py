from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.svm import SVC
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score, make_scorer
import score

data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])

normdata = normalize(data[:,:-1])

# prj = PCA(n_components = 100)
prj = LDA(n_components = 100)
# newdata = prj.fit_transform(normdata,data[:,-1])
# for i in range(5):
# 	print newdata[i]
# print len(newdata)
# print len(newdata[0])
# print np.shape(newdata)
print "data done"
print "logistic initialized"
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
dict = {}
dict[1] = 4
dict[2] = 1
maxf = 0
maxl = 0
maxscore = 0

skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle=True)
output =[]
finalscore = 0
counter = 0
for train, test in skf:
	counter = counter + 1
	newdata = prj.fit_transform([ normdata[i][:] for i in train ],[ data[i][-1] for i in train ])
	newtestdata = prj.transform([ normdata[i][:] for i in test ])
	clf = SVC(class_weight = dict, kernel = 'poly', degree = 5, coef0 = 3)
	clf = clf.fit(newdata, [ data[i][-1] for i in train ])
	prediction = clf.predict(newtestdata)
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	xscore = score.get_score( prediction, [ data[i][-1] for i in test ])
	finalscore = finalscore + xscore
	print xscore
	print "done"

finalscore = finalscore*(1.0)/counter
print finalscore