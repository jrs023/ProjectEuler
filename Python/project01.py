#ProjectEuler Number 1
#by Josh Smith

sum = 0
for i in range(0,1000):
    if(i%3 == 0 or i%5 == 0):
	sum = sum + i

print sum
