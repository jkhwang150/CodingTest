def solution(clothes):
    answer = 1
    # 해쉬 테이블 생성
    closet = {}
    
    for name,kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]

    for _, value in closet.items():
        answer *= (len(value) + 1)
        
    return answer -1
