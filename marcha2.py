t = input ()
for i in range (t) : 
	raw_input ()
	number = map (int, raw_input().split ())
	stems = 1.0 
	for leaves in number : 
		stems -= leaves 
		if stems < 0 : 
			print "No"
			break 
		stems *= 2 
	else  : 
		if (stems == 0) :
			print "Yes"
		else : 
			print "No"
