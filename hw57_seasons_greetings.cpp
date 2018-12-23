//Name: Dante Rivera
//Date: November 2018
//Takes user input as an integer, says a greetings based on season as number is equal to month of year
//Assignment literally broken


#include <iostream>

using namespace std;

int main()
{
	int month;
	cin >> month;
	
	if(month < 3 || month > 11){
		cout << "Happy Winter" << endl;
	}
	else if(month >= 3 && month < 7){
		cout << "Happy Spring" << endl;
	}
	else if(month >= 7 && month < 9){
		cout << "Happy Summer" << endl;
	}
	else{
		cout << "Happy Fall" << endl;
	}
	return 0;
}