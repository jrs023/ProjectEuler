#ProjectEuler Number 6
#by Josh Smith

n = 0
for i in xrange(1, 101):
	t = i*i
	n = n + t
	print t, " ", n

SquareOfSums = 0
p = 0
for i in xrange(1, 101):
	p = p + i

SquareOfSums = p*p

print SquareOfSums - n
