#include<stdio.h>

int main ()
{
	long long int t , n  ; 
	scanf ("%lld",&t) ;
	while(t--)
	{
		scanf ("%lld",&n) ;
		if (n%2 == 0 )
			printf ("ALICE\n");
		else 
			printf ("BOB\n");

	}
return 0 ;
}