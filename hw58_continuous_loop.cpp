//Name: Dante Rivera
//Date: November 2018
//Asks user for year of birth, if it's a future year it continues to ask them for an actual year they were born


#include <iostream>

using namespace std;

int main()
{
	int a = true;
	int b_year;
	
	while(a = true) {
		cout << "Please enter year born: " << endl;
		cin >> b_year;
		if(b_year > 2018){
			cout << "Entered a future year" << endl;
		}
		else if (b_year <= 2018){
			cout << "You entered: " << b_year << endl;
      return 0;
		}
	}
	return 0;
}
