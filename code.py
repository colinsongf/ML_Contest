import math as math

fp = open("/home/jpsagarm95/Desktop/ml_contest/ML-contest-training/contest_train.csv")
datastore = fp.read()
fp.close

totalData = []
totalNumberOfRows = len(datastore.split('\n')) - 1

temp = datastore.split('\n')
totalNumberOfColumns = len(temp[0].split(','))

for i in range(totalNumberOfRows):
	totalData.append([])
	for j in temp[i].split(','):
		totalData[i].append(float(j))


inputData = []
outputData = []
for i in range(totalNumberOfRows):
	inputData.append([])
	outputData.append(totalData[i][totalNumberOfColumns - 1])
	for j in range(totalNumberOfColumns - 1):
		inputData[i].append(totalData[i][j])

oneCounter = 0
twoCounter = 0
for i in range(totalNumberOfRows):
	if outputData[i] == 1:
		oneCounter = oneCounter + 1
	elif outputData[i] == 2:
		twoCounter = twoCounter + 1
	else:
		print outputData[i]

labelOneInputData = []
labelTwoInputData = []
for i in range (totalNumberOfRows):
	if outputData[i] == 1:
		labelOneInputData.append(inputData[i])
	else:
		labelTwoInputData.append(inputData[i])

rowsOfLabelOne = len(labelOneInputData)
rowsOfLabelTwo = len(labelTwoInputData)



meanFeaturesForLabelOne = []
for i in range(totalNumberOfColumns - 1):
	temp = 0
	counter = 0
	for j in range(rowsOfLabelOne):
		if(math.isnan(labelOneInputData[j][i])):
			counter = counter + 1
			temp = temp + labelOneInputData[j][i]
	if(counter != 0):
		meanFeaturesForLabelOne.append((temp/counter))
	else:
		meanFeaturesForLabelOne.append(0)


meanFeaturesForLabelTwo = []
for i in range(totalNumberOfColumns - 1):
	temp = 0
	counter = 0
	for j in range(rowsOfLabelTwo):
		if(math.isnan(labelTwoInputData[j][i])):
			counter = counter + 1
			temp = temp + labelTwoInputData[j][i]
	if(counter != 0):
		meanFeaturesForLabelTwo.append((temp/counter))
	else:
		meanFeaturesForLabelTwo.append(0)

labelOneInputDataNew = []
for i in range(rowsOfLabelOne):
	labelOneInputDataNew.append([])
	for j in range(totalNumberOfColumns - 1):
		if(math.isnan(labelOneInputData[i][j])):
			labelOneInputDataNew[i].append(meanFeaturesForLabelOne)
		else:
			labelOneInputDataNew[i].append(labelOneInputData[i][j])

labelTwoInputDataNew = []
for i in range(rowsOfLabelTwo):
	labelTwoInputDataNew.append([])
	for j in range(totalNumberOfColumns - 1):
		if(math.isnan(labelTwoInputData[i][j])):
			labelTwoInputDataNew[i].append(meanFeaturesForLabelTwo)
		else:
			labelTwoInputDataNew[i].append(labelTwoInputData[i][j])

