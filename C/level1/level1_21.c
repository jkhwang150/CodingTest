// 음양 더하기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// absolutes_len은 배열 absolutes의 길이입니다.
// signs_len은 배열 signs의 길이입니다.
int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int answer = 0;
    int arr[signs_len];
    for(int i=0;i<signs_len;i++){
        if(signs[i]==true){
        arr[i] = 1;
        }
        else{
        arr[i] = -1;
        }
    }
    for(int j=0;j<absolutes_len;j++){
        answer = answer + (absolutes[j] * arr[j]);
    }
    return answer;
} */

// 내적
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// a_len은 배열 a의 길이입니다.
// b_len은 배열 b의 길이입니다.
int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int answer =0;
    for(int i=0;i<a_len;i++){
        answer += a[i]*b[i];
    }
    return answer;
} */

// 소수 만들기
/* #include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int R_number(int x);
// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int count = 0;
    int n = 0;
    for(int i=0;i<nums_len;i++){
        for(int j=i+1;j<nums_len;j++){
            for(int k=j+1;k<nums_len;k++){
                n = nums[i]+nums[j]+nums[k];
                count = count + R_number(n);
            }
        }
    }
    return count;
}

int R_number(int x){
    int count = 0;
    for(int i=1;i<=x;i++){
        if(x%i==0) count++;
    }
    if(count == 2){
        return 1;
    }
    else return 0;
} */