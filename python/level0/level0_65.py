# 유한소수 판별하기
def Rn(a):
    count = 0
    for i in range(1,a+1):
        if(a%i==0):
            count+=1
    if count==2:
        return True
    else:
        return False
def Di(a,b):
    c = []
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0):
            c.append(i)
    return max(c)

def Dio(a):
    c = []
    for i in range(2,a+1):
        if(a%i==0):
            c.append(i)
    return c

def solution(a,b):
    if(a%b==0):
        return 1
    c = b//Di(a,b) # 분모를 최대 공약수로 나눈 수
    d = [[2,5],[2],[5]] # 기약분수의 조건
    # c의 약수 중 소수만 선택
    e = Dio(c)
    f = []
    for i in e:
        if(Rn(i)==True):
            f.append(i)
    if(f in d):
        return 1
    else:
        return 2
    

# 저주의 숫자 3
import math

def solution(n):
    
    count = 0
    for i in range(1,n+1):
        count+=1
        while count%3 == 0 or '3' in str(count):
            count+=1
    return count

# 외계어 사전
def solution(spell, dic):
    answer = 0
    count =0
    print(len(spell))
    for i in dic:
        for j in spell:
            if j in i:
                count+=1
                print(i)
        if count==len(spell):
            answer +=1
        count = 0
    if answer == 0:
        return 2
    else:
        return 1
    
# 삼각형의 완성조건(2)
def solution(sides):
    answer = []
    for i in range(1,max(sides)+1):
        if(min(sides)+i>max(sides)):
            answer.append(i)
    for j in range(max(sides),sum(sides)):
        if(sum(sides)>i):
            answer.append(j)
    answer2=set(answer)        
    a = list(answer2)
    print(a)
    return len(answer2)

# 숨어있는 숫자의 덧셈(2)
import re
def solution(my_string):
    answer = re.findall(r"[0-9]+",my_string)
    answer_sum =0
    for i in answer:
        answer_sum += int(i)
    return answer_sum