# 나이 출력
def solution(age):
    answer = 2023 - age
    return answer

# 아이스 아메리카노
def solution(money):
    answer = []
    a = 0
    for i in range(1,money):
        if(money//5500>0):
            a += 1
            money -=5500
        else:
            break
    answer.append(a)
    answer.append(money)
    return answer

# 옷가게 할인 받기
def solution(price):
    if(100000<=price<300000):
        return int(price-(price*0.05))
    elif(300000<=price<500000):
        return int(price-(price*0.1))
    elif(500000<=price):
        return int(price-(price*0.2))
    else:
        return int(price)
    
# 배열의 평균값
def solution(numbers):
    answer = 0
    return sum(numbers)/len(numbers)

# 피자 나눠 먹기(3)
def solution(slice, n):
    answer = 0
    for i in range(1,n+1):
        if(slice*i>=n):
            answer = i
            break
    return answer
