//ProjectEuler Number 5
//by Josh Smith

#include <iostream>
using namespace std;

bool divisble(size_t n){
	for(size_t i = 1; i <= 20; i++){
		if(n%i != 0)
			return false;
	} 
	return true;
}

int main() {
	size_t n = 1;
	
	while(!divisble(n)){
		n++;
	}
	
	cout << n << endl;
	return 0;
}
