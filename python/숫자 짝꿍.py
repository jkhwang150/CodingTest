# 첫번째 풀이
# 테스트 케이스 11~15오류(시간 초과)
def solution(X, Y):
    a = list(map(str,X))
    b = list(map(str,Y))
    c = []
    for i in a:
        if i in b:
            c.append(i)
            b.remove(i)
    c.sort(reverse = True)
    print(c)
    
    if c == []:
        return "-1"
    elif c[0] == "0":
        return "0"
    else:
        return ''.join(map(str, c))


# 피드백 후 풀이
# 나온 숫자를 카운트하여 풀이

def solution(X, Y):
    result = ''
    a = [0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0]
    
    for i in X:
        value = int(i)
        a[value] += 1
    
    for i in Y:
        value = int(i)
        b[value] += 1
    
    for i in range(9,-1,-1):
        value = str(i) * min(a[i],b[i])
        result += value
 
    if(len(result) == 0):
        return '-1'
    if(result[0] == '0'):
        return '0'
              
    return result
