def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        # 햄버거 완성 조건을 만족하면 Count에 1을 더한 후 삭제
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt
