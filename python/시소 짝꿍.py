# 첫번째 접근 > 시간 초과
def solution(weights):
    answer = 0
    weights.sort()
    c = []
    for i in range(0,len(weights)):
        for j in range(i+1,len(weights)):            
            if weights[i] == weights[j]:
                answer+=1
            elif weights[i]*3 == weights[j]*2:
                answer+=1
            elif weights[i]*2 == weights[j]:
                answer+=1
            elif weights[i]*4 == weights[j]*3:
                answer+=1
    
    return answer


# 두 번째 접근 > Counter를 사용하여 각 비율마다 카운트
from collections import Counter


def solution(weights):
    answer = 0
    
    # 1:1
    counter = Counter(weights)
    for k,v in counter.items():
        if v>=2:
            answer+= v*(v-1)//2
    weights = set(weights) 
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer
