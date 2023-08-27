# 자릿수 더하기
def solution(n):
    a = str(n)
    answer = 0
    for i in range(0,len(a)):
        answer += int(a[i])
        
    return int(answer)

# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if(i%n==0):
            answer.append(i)
    return answer

# 숫자 찾기
def solution(num, k):
    m = list(map(int,str(num)))
    print(m)
    for i in m:
        if(i==k):
            return m.index(i)+1
            break
    return -1

# 배열의 유사도
def solution(s1, s2):
    answer = 0
    return len(set(s1)&set(s2))

# 문자열 계산하기
def solution(my_string):
    answer = 0
    s = my_string.split()
    arr=int(s[0])
    for i in range(1,len(s),2):
        if(s[i]=='+'):
            arr += int(s[i+1])
        else:
            arr -= int(s[i+1])
    return arr

# 가장 큰 수 찾기
def solution(array):
    m = max(array)
    n = 0
    for i in range(0,len(array)):
        if(array[i]==m):
            n = i
            break
    
    return [m,n]

# 약수 구하기 
def solution(n):
    answer = []
    for i in range(1,n+1):
        if(n%i==0):
            answer.append(i)
    return answer

# 한 번만 등장한 문자
def solution(s):
    answer = ''
    c = []
    count = 0
    e = list(map(str,s))
    for i in e:
        for j in e:
            if(i==j):
                count += 1
        if(count==1):
            c.append(i)
        count = 0
    print(c)
    c.sort()
    return "".join(c)

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    lis = list(my_string)
    lis[num1],lis[num2] = lis[num2],lis[num1]
    return "".join(lis)

# 영어가 싫어요
def solution(numbers: str) -> int:
    return int(numbers.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0"))
