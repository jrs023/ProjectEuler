#ProjectEuler Number 3
#by Josh Smith

#My original solution that works, but DOES NOT WORK FOR LARGE NUMBERS
max = 1
iter = 0
value = 13195
temp = 0

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

print value
for i in xrange(1, value/2): 
    if(value%i == 0):
	temp = value/i
	boolean = is_Prime(temp)
	
    iter = iter + 1
    print iter
    if(boolean == True and temp > max):
	max = temp
print max
'''

#Optimal Solution that was derived from some googling, works for large numbers
n = 600851475143
i = 2
#This algorithm is based off the following fact
#the largest prime factor will never be greater than the square root of n

while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print n'''
