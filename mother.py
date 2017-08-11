import os
#a = os.getcwd()
#print a 
for i in range(1,50):
	fp = open("%d.py" % i, "w")
	fp.close()