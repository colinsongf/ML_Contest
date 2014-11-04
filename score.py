
# harmonic mean of the f1 scores of the 2 classes
def get_score(prediction, actual):
	positive = 1
	negative = 2
	tp = 0.0
	fp = 0.0
	tn = 0.0
	fn = 0.0
	for (GOT,IS) in zip(prediction, actual):
		if GOT == positive and IS == GOT:
			tp += 1
	for (GOT,IS) in zip(prediction, actual):
		if GOT == positive and IS != GOT:
			fp += 1
	for (GOT,IS) in zip(prediction, actual):
		if GOT == negative and IS != GOT:
			fn += 1
	for (GOT,IS) in zip(prediction, actual):
		if GOT == negative and IS == GOT:
			tn += 1
	score = 1/(1+((tp+tn)*(fp+fn)/(4*tp*tn)))
	return score
