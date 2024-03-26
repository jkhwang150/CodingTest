# 풀이 1.
def solution(k, tangerine):
    answer = 0
    dic={} #딕셔너리 만들기
    for i in list(set(tangerine)):
        dic[i]=0
    for i in tangerine: # 숫자만큼 딕셔너리 추가
        dic[i]+=1
    # dic=sorted(dic.items(),key=lambda x:x[0],reverse=True)    
    print(dic)
    dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(dic)
    cnt=0
    for i in dic: #정렬된 딕셔너리로 귤 개수 맞추기
        if cnt+i[1]<k:
            cnt+=i[1]
            answer+=1
        elif cnt+i[1]==k:
            return answer+1
        else:
            return answer+1

# 풀이 2.
from collections import Counter

def solution(k, tangerine):
    answer= 0 
    #Counter를 이용하여 요소, 요소의 갯수로 딕셔너리 생성
    counter = Counter(tangerine)

    sort_ = sorted(counter.items(), key = lambda x:x[1], reverse=True)

    cnt = 0
    for i in sort_:
        k-= i[1]
        answer +=1
        if k<=0:
            break
    return answer
