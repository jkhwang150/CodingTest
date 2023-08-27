# 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer

# 나이 출력
def solution(age):
    answer = 2023 - age
    return answer

# 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer

# 두 수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 숫자 비교하기
def solution(num1, num2):
    if(num1==num2):
        return 1
    else:
        return -1
    
# 몫 구하기
def solution(num1, num2):
    answer = num1//num2
    return answer

# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    answer = '%d'%((num1/num2)*1000)
    
    return int(answer)

# 각도기
def solution(angle):
    if(0<angle<90):
        return 1
    elif(angle==90):
        return 2
    elif(90<angle<180):
        return 3
    elif(angle == 180):
        return 4
    
# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if(i%2==0):
            answer+=i
    return answer
