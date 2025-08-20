#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    // the number of temperatures to analyse
    int n;
    scanf("%d", &n);
    if (n==0){
        printf("0");
        return 0;
    }
    int max = 999999999;
    int the_good = 0;
    for (int i = 0; i < n; i++) {
        // a temperature expressed as an integer ranging from -273 to 5526
        int t;
        scanf("%d", &t);
        if (t < 0){
            if (-t < max){
                max = -t;
                the_good = t;
            }
        } else{
            if (t <= max){
                max = t;
                the_good = t;
            }
        }
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d", the_good);

    return 0;
}
