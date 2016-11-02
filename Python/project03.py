#ProjectEuler Number 3
#by Josh Smith

n = 600851475143
i = 2
#This algorithm is based off the following fact
#the largest prime factor will never be greater than the square root of n

while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print n
