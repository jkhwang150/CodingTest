from itertools import product

def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U'] # 모음 5가지
    for i in range(1,6):
        for per in product(li,repeat = i): # 중복 순열의 개수를 1개부터 5개까지 생성
            answer.append(''.join(per)) # 순열을 문자열로 합친다.
    answer.sort() # 사전을 정렬한다
    return answer.index(word)+1 # 찾는 단어의 인덱스에 1을 더하여 순서를 구한다. (리스트는 0부터시작)
