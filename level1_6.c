// 나머지가 1이 되는 수 찾기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    for(int x=1;x<n;x++){
        if(n%x==1){
        answer=x;
        break;
        }
    }
    return answer;
} */

// 약수의 합
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    for(int i=1;i<=n;i++){
        if(n%i==0){
            answer=answer+i;
        }
        
    }
    return answer;
} */

// 평균 구하기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
double solution(int arr[], size_t arr_len) {
    double answer = 0;
    
    for(int i=0;i<arr_len;i++){
        answer = answer + arr[i];
        
    }
    answer = answer/arr_len;
    return answer;
} */