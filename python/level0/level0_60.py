# 암호 해독
def solution(cipher, code):
    answer = cipher[code-1::code]
    return "".join(answer)

# 369게임
def solution(order):
    answer = 0
    
    lis = list(str(order))
    lis2 = list('369')
    for i in lis:
        for j in lis2:
            if(i==j):
                answer+=1
    return answer

# 가까운 수
def solution(array, n):
    answer = []
    array.sort()
    for i in range(0,len(array)):
        answer.append(abs(n-array[i]))
        
    a = answer.index(min(answer))    
    return array[a]

# 중복된 문자 제거
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

# k의 개수
def solution(i, j, k):
    count = 0
    for a in range(i,j+1):
        n = list(map(int,str(a)))
        for m in n:
            if(m==k):
                count+=1
    return count

# A로 B 만들기
def solution(before, after):
    a = list(before)
    b = list(after)
    a.sort()
    b.sort()
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            return 0
            break
        else:
            continue
    return 1


# 이진수 더하기
def solution(bin1, bin2):
    answer = ''
    a = int(bin1,2)
    b = int(bin2,2)
    print(a,b)
    c = a+b
    answer = bin(c)
    return answer.replace('0b',"")

# 치킨 쿠폰
def solution(chicken):
    answer = -1
    count = 0
    cou = 0
    while(chicken!=0):
        chicken -=1
        count+=1
        if(count==10):
            chicken+=1
            cou+=1
            count=0
    return cou

# 로그인 성공?
import re
def solution(id_pw, db):
    for i in range(0,len(db)):
        
        if(db[i][0]==id_pw[0]):
            if(db[i][1]==id_pw[1]):
                return "login"
            else:
                return "wrong pw"
    return "fail"

# 등수 매기기
def solution(score):
    answer = []
    avg = []
    s =0
    for i in range(0,len(score)):
        for j in range(0,2):
            s += score[i][j]
        avg.append(s/2)
        s = 0
    print(avg)
    s_avg = sorted(avg,reverse=True)
    print(s_avg)
    rank = []
    for i in avg:
        rank.append(s_avg.index(i)+1)
    
    return rank