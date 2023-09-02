// 자연수 뒤집어 배열로 만들기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {
    
    int* answer = (int*)malloc(sizeof(int)*12);
    for(int i=0;n!=0;i++){
    answer[i] = n%10;
    n/=10;
    }
    return answer;
} */

//자릿수 더하기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    for(int i = n; i>0;i=i/10){
        answer=answer+i%10;
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