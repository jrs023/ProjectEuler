#ProjectEuler Number 4
#by Josh Smith


max = 0

for i in xrange(1000,100, -1):
	for j in xrange(1000,100, -1):
                string1 = str(i*j);
		string2 = string1[::-1]
		if string1 == string2 and i*j > max:
			max = i*j

print max

