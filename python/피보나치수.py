# 재귀로 풀이시 발생하는 런타임 오류를 잡음
def solution(n):
    answer = []
    for i in range(n+1):
        if i==0 or i==1:
            answer.append(i)
        else:
            f = answer[i-1] + answer[i-2]
            answer.append(f % 1234567)

    return answer[-1]
