#include<stdio.h>
#include<math.h>
 
int main ()
{
	float amount,rem ; 
	int drawl,check; // ranges from 0 to 2* 2^16 +1 
	scanf ("%d%f",&drawl,&amount);
	check = drawl % 5 ;
	if (drawl < amount && amount > (drawl+0.50))
	{
		if (check == 0)	
		{
			rem = amount - (drawl +0.50);
			printf ("%.2f",rem);
		}
		else
			printf("%.2f",amount);
	}
	else 
	printf ("%f",amount);
return 0;
}