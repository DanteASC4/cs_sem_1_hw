//Name: Dante Rivera
//Date: November 2018
//Prints Mihi cura futuri 10 times

// p = p + Bp - Dp
//p = population of said year
//B = birth rate of 12.4 births for every 1000 people each year, (12.4/1000)
//D = death rate of 8.4 deaths for every 1000 people (8.4/1000)
//Needs to estimate population for given number of years

#include <iostream>

using namespace std;

int main()
{
	int years;
	int last_pop = 325700000;
	int births;
	int deaths;
	int thousands;
	int total;
	
	for(int x = 1; x <= years; x++){
		thousands = last_pop%1000;
		births = 12.4 * thousands;
		deaths = 8.4 * thousands;
		total = last_pop + births - deaths
		
		cout << total << endl;
	}
	return 0;
}
