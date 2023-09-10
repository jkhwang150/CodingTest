# 3진법 뒤집기
def solution(n):
    answer = 0
    rev_3 = ''
    # 3진법 구해서 뒤집기
    while n>0:
        n, mod = divmod(n,3)
        rev_3 += str(mod)
        
    # 다시 10진법으로 표현하기
    answer = int(rev_3,3)
    
    return answer
