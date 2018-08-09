import re

fname = raw_input('Enter a file name\n')
try:
	fhand = open(fname)
except:
	print 'invalid file name : ', fname
	exit()
def transform(score):
	point = 0.0
	if score >= 90 and score <= 100:
		point = 4.0
	else: 
		if score >= 85 and score <= 89:
			point = 3.7
		else: 
			if score >= 82 and score <= 84:
				point = 3.3
			else: 
				if score >= 78 and score <= 81:
					point = 3.0
				else: 
					if score >= 75 and score <= 77:
						point = 2.7
					else: 
						if score >= 71 and score <= 74:
							point = 2.3
						else: 
							if score >= 66 and score <= 70:
								point = 2.0
							else: 
								if score >= 62 and score <= 65:
									point = 1.7
								else: 
									if score >= 60 and score <= 61:
										point = 1.3
									else: 
										if score >= 0 and score <= 59:
											point = 0.0
	return point

gradepoint = 0
allgrade = 0
for line in fhand:
	try:	
		find_grade = re.findall('^B.+([0-4]\.[0-9]+).+', line)
		find_score = re.findall('^B.+[0-4]\.[0-9]\s([0-9][0-9])', line)
		transformed_score = transform(float(find_score[0]))
		gradepoint = gradepoint + float(find_grade[0]) * transformed_score
		allgrade = allgrade + float(find_grade[0])
	except:
		continue
print 'GPA = ', gradepoint / allgrade



