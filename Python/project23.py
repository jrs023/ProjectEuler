def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


number = []
for i in range(1, 28124):
	n = factors(i)
	total = 0
	for j in n:
		if(j != i):
			total += j
	if total > i:
		number.append(i)

sums = []
for i in number:
	for j in number:
		if i+j not in sums:
			sums.append(i+j)
total = 0
for i in range(28124):
	if i not in sums:
		total += i
		
print total
