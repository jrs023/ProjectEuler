#ProjectEuler Number 5
#by Josh Smith

#original solution, very very slow. I had to find a better way
'''n = 232692560
bool = True
while bool == True:
	j = 0;
	for i in xrange(1,21):
		if(n%i != 0):
			break;
		else:
			j += 1
	print "N: ", n
	n += 1
	if(j == 20):
		bool = False

print n-1

'''

#optimal solution
def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)

n = 1
for i in xrange(1, 21):
    print n, i, lcm(n, i)
    n = lcm(n, i)
print n
