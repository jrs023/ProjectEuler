//ProjectEuler Number 3
//by Josh Smith

#include <iostream>
using namespace std;

int main() {
	size_t n = 600851475143;
	size_t i = 2;
	
	while(i*i < n){
		while(n%i == 0)
			n /= i;
		i++;
	}
	cout << n << endl;
	
	return 0;
}
