# 가장 가까운 글자
def solution(s):
    answer = []

    word_dict = {}

    for idx, word in enumerate(list(s)):
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = idx
        else:
            answer.append(idx - word_dict[word])
            word_dict[word] = idx
    return answer

# 추억 점수
def solution(name, yearning, photo):
    answer = []
    for i in range(0,len(photo)):
        s = 0
        for j in range(0,len(photo[i])):
            if photo[i][j] in name:
                c = name.index(photo[i][j])
                s += yearning[c]
        answer.append(s)
            
    return answer

# 크기가 작은 부분문자열
def solution(t, p):
    answer = 0
    c = []
    n = 0
    while(len(t)+1!=n+len(p)):    
        c.append(t[n:n+len(p):])
        n+=1
    for i in c:
        if(int(i)<=int(p)):
            answer+=1
    return answer
