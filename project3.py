#ProjectEuler Number 3
#by Josh Smith

max = 1
iter = 0
value = 600851475143
temp = 0

print value
for i in xrange(1, value/2): 
    if(value%i == 0):
	temp = value/i
	boolean = True
	for i in xrange(2, temp): 
		if temp%i == 0:
			boolean = False
			break;
    iter = iter + 1
    print (iter/value)*100.0, "%"
    if(boolean == True and temp > max):
	max = temp
print max
