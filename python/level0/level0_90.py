# 숫자 비교하기
def solution(num1, num2):
    if(num1==num2):
        return 1
    else:
        return -1
    
# 두 수의 나눗셈
def solution(num1, num2):
    answer = '%d'%((num1/num2)*1000)
    
    return int(answer)

# 몫 구하기
def solution(num1, num2):
    answer = num1//num2
    return answer

# 머쓱이보다 큰 사람
def solution(array, height):
    answer = 0
    for i in range(0,len(array)):
        if(array[i]>height):
            answer += 1
    return answer

# 중복된 숫자의 갯수
def solution(array, n):
    answer = 0
    for i in range(0,len(array)):
        if(array[i]==n):
            answer+=1
    return answer