# 최댓값 만들기(2)
def solution(numbers):
    pl = 0
    mi = 0
    numbers.sort()
    pl = numbers[0] * numbers[1]
    mi = numbers[-1] * numbers [-2]
    if(pl>mi):
        return pl
    else:
        return mi

# 캐릭터의 좌표
import math
def solution(keyinput, board):
    answer = [] 
    c = board[0]//2 # 가로 크기
    d = board[1]//2 # 세로 크기
    lotate = [0,0]
    for i in keyinput:
        if(i=="left"):
            lotate[0] -= 1
            if(lotate[0]<-c):
                lotate[0] = -c
        elif(i=="right"):
            lotate[0] +=1
            if(lotate[0]>c):
                lotate[0] = c
        elif(i=="up"):
            lotate[1] +=1
            if(lotate[1]>d):
                lotate[1] = d
        elif(i=="down"):
            lotate[1] -=1
            if(lotate[1]<-d):
                lotate[1]=-d
    
    
    
                
    return lotate

# 직사각형 넓이 구하기
import math
def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots] 
    return (max(x)-min(x))*(max(y)-min(y))

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in range(0,len(strlist)):
        answer.append(len(strlist[i]))
    return answer

# 컨트롤 제트
def solution(s):
    answer = 0
    t = s.split(' ')
    print(t)
    for i in range(0,len(t)):
        if(t[i]=='Z'):
            answer -= int(t[i-1])
        else:
            answer += int(t[i])
    return answer
