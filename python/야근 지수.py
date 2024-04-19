# 1번 풀이
# 큰 수들에서 1씩 빼가면서 야근지수를 구함
# 효율성 테스트 : 시간 초과
'''
def solution(n, works):
    answer = 0
    for i in range(n):
        works.sort()
        works[-1] -= 1
    
    for i in works:
        if i < 0:
            continue
        else:
            answer+= (i*i)
    return answer
  '''
# heapq를 이용한 풀이
# 반복문을 통해-heapq에 1씩 더하여 야근 지수를 구함

import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    return sum([w ** 2 for w in works])
