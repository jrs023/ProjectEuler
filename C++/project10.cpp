//ProjectEuler Number 10
//by Josh Smith

#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(size_t n){
	if(n < 0){
		cout << "n must be larger than zero" << endl;
		return false;
	}

	for(int i = 2; i < sqrt(n)+1; i++){
		if(n%i == 0){
			return false;
		}
	}
	return true;
}

int main() {
	
	size_t sum = 2;
	size_t x = 3;
	while(x <= 2000000){
		if(isPrime(x)){
			sum += x;
		}
		x++;
	}
	cout << sum << endl;
	return 0;
}
