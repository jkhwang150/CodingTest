# 주어진 문자열에서 'e' 'v' 'r' 뒤에 오는 숫자들을 합하여 월과 일을 표현하시오.

def solution(data):
    lis = list(data)
    num = 0
    for i in range(0,len(lis)):
      # 조건1,2) 특정 문자열 뒤 0~10사이의 숫자만 걸러야함.
        if (lis[i] == 'r' or lis[i] == 'e' or lis[i] =='v') and '0'<=lis[i+1]<='9':
            if lis[i+1] == '1':
                if lis[i+2] == '0':
                    num += 10
                else:
                    num += 1
            else:
                num += int(lis[i+1])
    a = num //10 # 몫 > 월
    b = num % 10 # 나머지 > 일
    return "{}월 {}일".format(a,b)
