#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int rank(int x);
// lottos_len은 배열 lottos의 길이입니다.
// win_nums_len은 배열 win_nums의 길이입니다.
int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    int* answer = (int*)malloc(sizeof(int) * 2);
    int best= 0;
    int worst = 0;
    // 최상의 결과
    for(int i=0;i<lottos_len;i++){
        for(int j=0;j<lottos_len;j++){
          if(lottos[i]==win_nums[j]){
            best++;
          } 
        }
      if(lottos[i]==0){
        best++;
      }
    }
    //최악의 결과
    for(int k=0;k<6;k++){
        for(int o=0;o<6;o++){
          if(lottos[k]==win_nums[o]){
            worst++;
        }
      }
    }
     answer[0] = rank(best);
     answer[1] = rank(worst);
    return answer;
    
}

int rank(int x){
  switch(x){
    case 0:
      return 6;
    case 1:
      return 6;
    case 2:
      return 5;
    case 3:
      return 4;
    case 4:
      return 3;
    case 5:
      return 2;
    case 6:
      return 1;
      default: return 7;
  }
}
