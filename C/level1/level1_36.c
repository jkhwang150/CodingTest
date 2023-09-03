// 문자열을 정수로 바꾸기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    answer = atoi(s);
    return answer;
}
 */
// 두 정수 사이의 합
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    long long answer2 = 0;
    if(a>b){
        for(int i=b;i<=a;i++){
            answer = answer +i;
        }
        return answer;
    }
    else if(b>a){
        for(int j=a;j<=b;j++){
            answer2 = answer2 +j;
        }
        return answer2;
    }
    else{
        return a;
    }
} */

// 가운데 글자 가져오기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(1);
    int i = strlen(s);
    if(i%2==0){
        answer[0] = s[i/2-1];
        answer[1] = s[i/2];
        answer[2] = '\0';
    }
    else{
        answer[0] = s[i/2];
        answer[1] = '\0';
    }
    return answer;
} */
