# 연속된 수의 합
def solution(num, total):
    answer = []
    d = total//num
    if(num%2==1):
        c = (num-1)/2
        for i in range(0,num):
            answer.append(d-c+i)
    else:
        c = num/2 -1
        for i in range(0,num):
            answer.append(d-c+i)
    return answer

# 종이 자르기  
def solution(M, N):
    if(M*N==1):
        return 0
    else:
        return M*N-1
    
# 문자열 밀기
def solution(A, B):
    answer = 0
    n = len(A) - 1
    c = []
    
    for i in range(0,n+1):
        c.append(A[-i::]+A[:-i:])
    print(c)
    if B in c:
        return c.index(B)
    else:
        return -1
    
# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    m = my_str
    s = len(m)
    i=0
    while(s/n>0):
        answer.append(my_str[i:i+n:])
        s = s - n
        i+=n
    return answer

# 7의 개수
def solution(array):
    answer = 0
    e = []
    for i in array:
        d = list(map(int,str(i)))
        for j in d:
            if(j==7):
                answer+=1
    print(e)
    return answer


# 문자열 정렬하기(2)
def solution(my_string):
    s = my_string.lower()
    answer = sorted(s)
    return "".join(answer)

# 세균 증식
def solution(n, t):
    for i in range(1,t+1):
        n = n * 2
    return n

# 제곱수 판별하기
def solution(n):
    answer = 0 
    for i in range(1,n+1):
        if(n/i==i):
            answer = 1
    
    if(answer==1):
        return 1
    else:
        return 2
    

# 문자열 안에 문자열
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        return 1
    else:
        return 2

# OX 퀴즈
def solution(quiz):
    answer = []
    
    for i in quiz:
        s = i.split(" ")
        fir =0
        if(s[1]=='-'):
            fir = int(s[0])-int(s[2])
        elif(s[1]=='+'):
            fir = int(s[0])+int(s[2])
        if(fir == int(s[4])):
            answer.append("O")
        elif(fir != int(s[4])):
            answer.append("X")
    return answer
