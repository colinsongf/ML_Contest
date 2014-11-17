import sys

#sys.argv[0] is the .py file
print sys.argv[1:]

files = [open(f) for f in sys.argv[1:]]
output = open('majority_vote7.txt', 'w')

for i in range(1500):
	AlessB=0
	for f in files:
		if f.readline().strip() == 'A':
			AlessB += 1
		else:
			AlessB -= 1
	if AlessB >= 0:
		output.write('A\n')
	else:
		output.write('B\n')
