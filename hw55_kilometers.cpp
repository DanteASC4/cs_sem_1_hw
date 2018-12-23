//Name: Dante Rivera
//Date: November 2018
//Takes user input as miles, converts to kilometers and returns it

#include <iostream>

using namespace std;

int main()
{
	int miles = 0;
	int kilos = 0;
	cin >> miles;


	kilos = miles * 0.621371; // Google says that a mile is about 1.6 kilos but this is what the question from my class is asking for


	cout << "Kilometers: " << miles *  0.621371 << endl;
	return 0;
}