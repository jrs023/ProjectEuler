count = 0;
prev_count = 0;
max_count = 0;
max = [];

for i in range (1, 1000000):
	x = i;
	count = 0;
	#print "I: " + str(i)
	while(x != 1):
		if(x%2 == 0):
			x = x/2;
		else:
			x = 3*x+1;
		#print str(x) + " " + str(count)
		count += 1;
	#print " "
	if count > max_count:
		max = i;
		max_count = count;
	
print max
print max_count
