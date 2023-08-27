# 과일 장수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    lis = []
    arr = []
    for i in range(0,len(score)//m):
        lis.append(min(score[m*i:m*(i+1)])*m)
    
    return sum(lis)

# 최소 직사각형
def solution(sizes):
    w = []
    h = []
    print(max(max(x) for x in sizes))
    print()
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if(i==j):
                continue
            else:
                answer.append(numbers[i]+numbers[j])
    result = list(set(answer))
    result.sort()
    return result
