#ProjectEuler Number 2
#by Josh Smith

sum = 0
fib = 0
x = 0
y = 1
while fib < 4000000:
    fib = x + y
    x = y
    y = fib
    if(fib%2 == 0):
	sum = sum + fib

print sum
