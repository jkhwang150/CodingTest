# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = [x]
    s = x
    for i in range(1,n):
        x = x + s
        answer.append(x) 
    return answer

# 행렬의 덧셈
def solution(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

# 최대공약수와 최소공배수
# 최대 공약수
def Di(a,b):
    c = []
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0):
            c.append(i)
    return max(c)

# 최소 공배수
def Mu(a,b):
    return a*b//Di(a,b)
    
def solution(n, m):
    return [Di(n,m),Mu(n,m)]
