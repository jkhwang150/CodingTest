# n이 만들어질 수 있는 경우의 수는 피보나치의 수와 같다.
def solution(n):
    answer = 0
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    # 따라서 n번째 피보나치 수를 1234567로 나누어준다.
    answer = b % 1234567
    return answer
