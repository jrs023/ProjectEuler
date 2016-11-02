def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))
            
        
f = open("names.txt", 'r')
listOfNames = (f.read()).split(',')
sortList = quicksort(listOfNames)

total = 0
for i in range(len(sortList)):
	if(sortList[i] != "\n"):
		for j in sortList[i]:
			if(j != '\"' and j!= "\n"):
				total += (i+1)*(ord(j)-64)
	
print total

