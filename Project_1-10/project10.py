#ProjectEuler Number 9
#by Josh Smith

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    
total = 0
for i in range(2, 2000000):
	if(is_prime(i) == True):
		total += i
		
print total
