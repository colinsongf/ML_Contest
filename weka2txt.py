import sys
print sys.argv
f = open(sys.argv[1])
g=open(sys.argv[2],'w')
for l in f:
	try:
		if l[25]=='1':
			g.write('A\n')
		elif l[25]=='2':
			g.write('B\n')
		else:
			g.write('C\n')
	except IndexError:
		print l
f.close()
g.close()
print "done"

