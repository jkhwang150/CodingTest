# 편지
def solution(message):
    answer = len(message)*2
    return answer

# 점의 위치 구하기
def solution(dot):
    if(dot[0]>0 and dot[1]>0):
        return 1
    elif(dot[0]>0 and dot[1]<0):
        return 4
    elif(dot[0]<0 and dot[1]>0):
        return 2
    else:
        return 3
    
# 문자열 곱하기
def solution(my_string, k):
    answer = ''
    answer = my_string * k
    
    print(answer)
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num%n==0:
        return 1
    else:
        return 0
    
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a + b
    else:
        return a - b
    
# 마지막 두 원소
def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        c = num_list[-1] - num_list[-2]
        answer.append(c)
    else:
        c = num_list[-1] * 2
        answer.append(c)
    return answer

# 대문자로 바꾸기.
def solution(myString):
    answer = myString.upper()
    
    return answer

# 정수 부분
def solution(flo):
    answer = int(flo)
    return answer

# 문자열을 정수로 변환하기
def solution(n_str):
    answer = int(n_str)
    return answer 

# 다음에 올 숫자
def solution(common):
    answer = 0
    a = common[1] - common[0]
    b = common[-1] - common[-2]
    if(a==b):
        answer = common[-1] + a
    else:
        answer = common[-1]*(common[-1]//common[-2])
    return answer
