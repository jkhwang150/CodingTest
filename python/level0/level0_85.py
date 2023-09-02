# 피자 나눠 먹기(2)
def solution(n):
    answer = 0 
    for i in range(1,n+1):
        if((6*i)%n==0):
            answer = i
            break
    return answer

# 피자 나눠 먹기(1)
def solution(n):
    for i in range(1,n+1):
        if(7*i//n>0):
            return i
            break

# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(0,n+1):
        if(i%2==1):
            answer.append(i)
    return answer

# 중앙값 구하기
def solution(array):
    array.sort()
    
    return array[len(array)//2]

# 분수의 덧셈
import math
def solution(numer1, denom1, numer2, denom2):
    
    m = (denom1*numer2) + (denom2*numer1)
    n = denom1*denom2
    g = math.gcd(m,n)
    answer = [m/g,n/g]
    return answer