#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int n) {
    int answer = 0;
    while(1){
    if(n<a) break;
    answer = answer + ((n/a)*b);
    n = (n/a)*b + (n%a);
    }
    return answer;
}
