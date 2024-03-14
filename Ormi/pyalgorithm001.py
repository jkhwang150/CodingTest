# 주어진 문자열을 1과 0으로 바꾸고 아스키 코드표 안에 문자로 바꾸세요.

def solution(data):    
    # 입력을 2진수로 변환
    bi = []
    for i in range(0,len(data)):
        s = ''
        for j in data[i]:
            if j == '+':
                s += '1'
            elif j == ' ':
                continue
            else:
                s += '0'
        bi.append(s)

    # 2진수를 10진수로 변환
    de = []
    for i in bi:
        de.append(int(i,2))

    # 10진수를 아스키코드로 변환
    s =''
    for i in de:
        s += chr(i)
    return s
