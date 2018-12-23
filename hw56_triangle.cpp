//Name: Dante Rivera
//Date: November 2018
//Takes user input as an integer, draws a star once, incrementing by one until reaches the specified number

#include <iostream>

using namespace std;

int main()
{
	int max;
	cin >> max;
	
	for(int x = 1; x <= max; x++){
		for(int y = 1; y <= x; y++){
			cout << "*";
		}
		cout << "\n";
	}
	return 0;
}