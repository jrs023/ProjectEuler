#ProjectEuler Number 7
#by Josh Smith

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

bool = False
i = 2
j = 0
while j < 10001:
	if is_prime(i):
		j += 1
	i += 1
	
print i-1
