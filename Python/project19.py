start = [1, 1, 1900, 2]
count = 0;
while(start[0] != 12 or start[1] != 31 or start[2] != 2000):
	start[1] += 1
	start[3] += 1
	if(start[3] > 7):
		start[3] = 1
	if(start[0] == 9 or start[0] == 4 or start[0] == 6 or start[0] == 11):
		if(start[1] > 30):
			start[0] += 1
			start[1] = 1
	elif(start[0] == 2):
		if(start[2]%4 == 0 and start[1] > 29):
			start[0] += 1
			start[1] = 1
		elif(start[2]%4 != 0 and start[1] > 28):
			start[0] += 1
			start[1] = 1
	else:
		if(start[0] == 12):
			if(start[1] > 31):
				start[0] = 1
				start[1] = 1
				start[2] += 1
		else:
			if(start[1] == 32):
				start[0] += 1
				start[1] = 1
	if(start[2] >= 1901 and start[3] == 1 and start[1] == 1):
		count += 1	
print count
