def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

summation = 0
for i in range (10, 10000):
	j = factors(i)
	total1 = 0
	total2 = 0
	for x in j:
		total1 += x
	total1 -= i
	j = factors(total1)
	for x in j:
		total2 += x
	total2 -= total1
	if total2 == i and total2 != total1:
		summation += total2
		summation += i
		
print summation/2
