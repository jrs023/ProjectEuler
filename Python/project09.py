#ProjectEuler Number 9
#by Josh Smith

for x in range(1, 1000):
	for y in range(x+1, 1000):
		for z in range (y+1, 1000):
			if x*x + y*y == z*z and x+y+z == 1000:
				print str(x) + " " + str(y) + " " + str(z)
				print x*y*z
