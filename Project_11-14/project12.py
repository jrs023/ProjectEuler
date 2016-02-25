#ProjectEuler Number 12
#by Josh Smith


import math

def factors(n):    
    return len(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

n = 0
iter = 0
count = 0
while count <= 500:
	iter += 1
	n = n + iter
	i = 1
	count = factors(n)
	
print n
