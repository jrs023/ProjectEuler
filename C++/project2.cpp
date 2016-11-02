//ProjectEuler Number 2
//by Josh Smith

#include <iostream>
using namespace std;

int main() {
	int fTotal = 0;
	int fib;
	int x = 0;
	int y = 1;
	while(fib < 4000000){
		fib = x + y;
		x = y;
		y = fib;
		if(fib%2 == 0)
			fTotal += fib;
	}
	cout << fTotal << endl;
    
    return 0;
}
