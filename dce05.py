import math 
t = int (raw_input ())  
for i in range(t) : 
	n = int (raw_input ()) 
	i = 0 ;  
	while (n!=0): 
		n /= 2  
		i += 1  
	print pow (2 , i-1 )  