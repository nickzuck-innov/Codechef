k ,n =map(int , raw_input().split ()) 
a = []
for i in range (k): 
	temp  = raw_input () 
	a.append(temp)

for i in range (n) : 
	b = raw_input ()
	for j in range (k):
		if len(b) >= 47 :
			flag = 1 
			break 
		elif a[j] in b :
			flag = 1 
			break
		else :
			flag = 0 
	if flag ==1  : 
		print "Good"
	else :
		print "Bad"
	