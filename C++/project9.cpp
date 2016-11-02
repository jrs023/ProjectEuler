//ProjectEuler Number 9
//by Josh Smith

#include <iostream>
using namespace std;

int main() {
	for(int x = 1; x < 1000; x++){
		for(int y = 1; y < 1000; y++){
			for(int z = 1; z < 1000; z++){
				if((x*x + y*y) == z*z and x+y+z == 1000){
					cout << x*y*z << endl;
					return 0;
				}
			}
		}
	}
	return 0;
}
