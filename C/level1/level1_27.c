// 직사각형 별찍기
/* #include <stdio.h>

int main(void) {
    int a;
    int b;
    int j=1;
    scanf("%d %d", &a, &b);
    while(j<=b){
      
        for(int i=0;i<a;i++){
            printf("*");
            
        }
      printf("\n");
      j++;
    }
    return 0;
} */

// 핸드폰 번호 가리기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* phone_number) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(1);
    strcpy(answer,phone_number);
    for(int i=0;i<strlen(phone_number);i++){
        if(strlen(phone_number)-4 >i){
            answer[i] = '*';
        }
        
    }
    return answer;
} */

// 하샤드 수
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {  
    int answer =0;
    int i = x;
    bool sum = true;
    while(x!=0){
        answer = answer + (x%10);
        x = x/10;
    }
    if(i%answer==0){
        sum = true;
    }
    else{
        sum = false;
    }
    return sum;
} */