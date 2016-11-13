//ProjectEuler Number 7
//by Josh Smith

#include <iostream>
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
	size_t i = 0;
	size_t x = 2;
	while(i <= 10001){
		if(isPrime(x)){
			i++;
		}
		x++;
	}
	cout << x-1 << endl;
	return 0;
}
