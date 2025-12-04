#include <stdio.h>

int main(void)
{
    // Interger: 1, 2, 3, -1 , 0, int -> %d
    // whole numbers: 1.2, 4.5, 3.1415, float -> %f
    // characters: 'a', 'b', '#', '@' -> char -> %c

    int number;

    printf("Number: ");
    scanf("%d", &number);

    printf("output: %d\n", number);
}