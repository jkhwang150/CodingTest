# 소인수분해
def solution(n):
    answer = []
    a = []
    for i in range(1,n+1):
        if(n%i==0):
            answer.append(i)
    lis = set(answer)
    for i in lis:
        if(RealNum(i)==True):
            a.append(i)
    return a
    

def RealNum(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
    
# 숨어있는 숫자의 덧셈
def solution(my_string):
    answer = 0
    
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

# 문자열 정렬하기(1)

def solution(my_string):
    answer = []
    for i in my_string:
        if(i.isdigit()):
            answer.append(int(i))
    answer.sort()
    return answer

# 모음 제거
def solution(my_string):
    ae = "a,e,i,o,u"
    for j in ae:
        my_string = my_string.replace(j,"")
    return my_string

# 팩토리얼
import math

def solution(n):
    for i in range(10,0,-1):
        if(math.factorial(i)<=n):
            return i
            break