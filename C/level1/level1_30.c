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

// 콜라츠 추측
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    int answer = 0;
    long n = num;
    while(n!=1){
        if(n%2==0){
            n = n / 2;
            answer++;
            }
        else{
            n = (n*3) +1;
            answer++;
        }
    }
    if(answer>500){
        return -1;
    }
    else{
        return answer;
    }
} */

// 정수 제곱근 판별
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long n) {
    long long answer = 0;
    long long temp=0;
    for(long long i=1;i<=n;i++){
        if(n/i==i&&n%i==0){
        answer = (i+1)*(i+1);
            break;
        }
        else{
            answer = -1;
        }
    }
    return answer;
} */