// 삼총사
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// number_len은 배열 number의 길이입니다.
int solution(int number[], size_t number_len) {
    int answer = 0;
    int sum = 0;
    for(int i=0;i<number_len;i++){
        for(int j=i+1;j<number_len;j++){
            for(int k=j+1;k<number_len;k++){
                if(number[i] + number[j] + number[k]==0) answer++;
                
            }
        }
    }
    return answer;
} */

// 콜라 문제
/* #include <stdio.h>
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
} */

// 없는 숫자 더하기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = -1;
    int total = 45;		//0부터 9까지 모두 더한 값
    int sum = 0;	//numbers의 값의 합을 저장하기 위한 변수
    
    for(int i=0;i<numbers_len;i++){
        sum = sum + numbers[i];
    }
    answer = total - sum;
    return answer;
} */