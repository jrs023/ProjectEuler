#a function to spell out numbers in words
def spellnum(num,join=True):
	thousands = ['','thousand','million']
        tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
        teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
        units = ['','one','two','three','four','five','six','seven','eight','nine'] 
        #Empty List for number words
    	words = [] 
        num = abs(num)
        #a series of steps to process the numbers and turn them into words
    	numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundredand')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g])
        #final joining of parts
    	if join: return ''.join(words)
        return words
        
total = 0
for i in range(1,1001):
	print str(total) + " " + spellnum(i) + " " + str(len(spellnum(i)))
	total += len(spellnum(i))
	#print total
	
print total-(9*3)
