//ProjectEuler Number 6
//by Josh Smith

#include <iostream>
using namespace std;

size_t sumOfSquares(size_t n){
	size_t sum = 0;
	for(size_t i = 0; i <= n; i++){
		sum += i*i;
	}
	return sum;
}

size_t squareOfSums(size_t n){
	size_t sum = 0;
	for(size_t i = 0; i <= n; i++){
		sum += i;
	} 
	return sum*sum;
}

int main() {
	cout << squareOfSums(100) - sumOfSquares(100) << endl;
	return 0;
}
