# 덧칠하기
def solution(n, m, section):
    answer = 1 # 최소 한번은 칠해야함
    paint = section[0] # 덧칠 시작점
    for i in range(1,len(section)):
        if section[i] - paint >= m:  # 덧칠 섹션이 m(붓 크기)를 넘어가면 횟수를 1 늘리고 덧칠 끝점을 다시 시작점으로 
            answer +=1
            paint = section[i]
    return answer
