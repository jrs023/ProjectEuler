//ProjectEuler Number 11
//by Josh Smith

#include <iostream>
#include <fstream>
using namespace std;

//Just to make the code more readable
int down(int val1, int val2, int val3, int val4){ return val1*val2*val3*val4;}
int right(int val1, int val2, int val3, int val4){ return val1*val2*val3*val4;}
int diagonal1(int val1, int val2, int val3, int val4){ return val1*val2*val3*val4;}
int diagonal2(int val1, int val2, int val3, int val4){ return val1*val2*val3*val4;}
int max_value(int val1, int val2, int val3, int val4){
	int array[4] = {val1, val2, val3, val4};
	int max = -5;
	for(int i = 0; i < 4; i++){
		if(array[i] > max){
			max = array[i];
		}
	}
	return max;
}


int main() {
	int array[20][20] = {0};

	ifstream numbers;
	numbers.open("project11.txt");
	
	int temp;
	for(int i = 0; i < 20; i++){
		for(int j = 0; j < 20; j++){
			numbers >> temp;
			array[i][j] = temp;
		}
	}
	
	int max = 0;
	for(int i = 0; i < 20; i++){
		for(int j = 0; j < 20; j++){
			int val1 = -5;
			int val2 = -5;
			int val3 = -5;
			int val4 = -5;
			if(i < 17)
				val1 = down(array[i][j], array[i+1][j], array[i+2][j], array[i+3][j]);
			if(j < 17)
				val2 = right(array[i][j], array[i][j+1], array[i][j+2], array[i][j+3]);
			if(i < 17 and j < 17)
				val3 = diagonal1(array[i][j], array[i+1][j+1], array[i+2][j+2], array[i+3][j+3]);
			if(i > 3 and j < 17)
				val4 = diagonal2(array[i][j], array[i-1][j+1], array[i-2][j+2], array[i-3][j+3]);
			
			int temp = max_value(val1, val2, val3, val4);	
			if(temp > max){
				max = temp;
			}
		}
	}
	
	cout << max << endl;
	numbers.close();
	return 0;
}
