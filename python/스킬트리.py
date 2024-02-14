def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        s = ''
        for i in tree:
            if i in skill:  # 선행스킬에 포함된다면
                s += i
        if skill[:len(s)] == s:  # skill의 앞부터 s의 길이만큼 s와 같다면 
            answer += 1  # 가능한 스킬트리
        print(s)
    return answer
