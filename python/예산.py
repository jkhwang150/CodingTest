def solution(d, budget):
    answer = 0
    real = 0
    d.sort()
    for i in d:
        real += i
        if real <=budget:
            answer += 1
        else:
            break
    return answer
