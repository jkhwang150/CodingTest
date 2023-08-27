# 배열의 평균값
def solution(numbers):
    answer = 0
    return sum(numbers)/len(numbers)

# 양꼬치
def solution(n, k):
    i = n
    while(n//10!=0):
        if(n>=10):
            k-=1
            n-=10
    return 12000*i + 2000*k

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in range(0,len(strlist)):
        answer.append(len(strlist[i]))
    return answer

# 삼각형의 완성조건(1)
def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    if(sides[0]<sides[1]+sides[2]):
        return 1
    else:
        return 2
    
# 짝수 홀수 개수
def solution(num_list):
    answer = []
    a=0
    b=0
    for i in range(len(num_list)):
        if(num_list[i]%2==0):
            b+=1
        else:
            a+=1
    answer.append(b)
    answer.append(a)
    
    return answer

# 배열 뒤집기
def solution(num_list):
    answer = num_list[len(num_list)::-1]
    return answer

# 배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        answer.append(numbers[i]*2)
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in range(0,len(array)):
        if(array[i]>height):
            answer += 1
    return answer

# 피자 나눠 먹기(1)
def solution(n):
    for i in range(1,n+1):
        if(7*i//n>0):
            return i
            break
