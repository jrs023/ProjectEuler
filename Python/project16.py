import math

value = pow(2, 1000)
string = str(value)
total = 0

for i in string:
	total += int(i)

print total
