#include <stdio.h>

int main() {
	int number, max, power, step;

	number = 0;
	max = 100;
	power = 0;
	step = 2;

	while(number <= max){
		power = number * number * number;
		printf("Number: %d, power: %d\n", number, power);
		number += step;
	}
}
