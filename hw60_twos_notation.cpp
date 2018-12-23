//Name: Dante Rivera
//Date: December 2018
//Asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation

#include <iostream>

using namespace std;
int main() {
  int a = 0;
  int x = 0;
  int b = 16;

  cin >> a;
  
  if (a < 0){
    cout << 1;
    x = 32 + a;
  }
  else {
    cout << 0;
    x = a;
  }


  while (b > 0.5){
    if(x >= b){
      cout << 1;
    }
    else {
      cout << 0;
    }
    x = x%b;
    b = b/2;
  }


}