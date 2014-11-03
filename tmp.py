f1 =open('/home/jpsagarm95/workspace/ml_2/iris.data.txt')
f2=open('/home/jpsagarm95/workspace/ml_2/iris.data2.txt', 'w')
line=f1.readline()
x=line.count(',')
for i in range(x):
	f2.write('Att' + str(i+1) + ',')
f2.write('CLASS\n')
f2.write(line)
for line in f1:
	f2.write(line)

f1.close()
f2.close()