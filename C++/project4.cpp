//ProjectEuler Number 4
//by Josh Smith

#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(int n){
	string s = std::to_string(n);
	for(int i = 0; i < s.length()/2; i++){
		if(s[i] != s[s.length()-1-i])
			return false;
	} 
	return true;
}

int main() {
	int max = 0;
	
	for(int i = 999; i > 99; i--){
		for(int j = 999; j > 99; j--){
			if(isPalindrome(i*j)){
				if(i*j > max){
					max = i*j;
				}
			}
		}
	}
	cout << max << endl;
	
	return 0;
}
