# 제일 작은 수 제거하기
import copy

def solution(arr):
    lis = copy.deepcopy(arr)
    lis.sort()
    d = lis[0]
    if(arr == [10]):
        return [-1]
    else:   
        arr.remove(d)
        return arr
    
# 정수 내림차순으로 배치하기
def solution(n):
    nlist = list(str(n))
    nlist.sort(reverse=True)
    answer = int("".join(nlist))
    return answer

# 수박수박수박수박수박수?
def solution(n):
    answer = []
    for i in range(n,0,-1):
        if(i==0):
            break
        elif(i%2==1):
            answer.append('수')
        elif(i%2==0):
            answer.append('박')
    answer.reverse()
    lis = ("".join(answer))  
    return lis

