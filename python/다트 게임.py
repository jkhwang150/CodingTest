def solution(r):
    answer = 0
    dart = list(r)
    num = []
    
    for i in range(0,len(dart)):   
        s = 0
        # 점수는 0~10사이의 정수이다.
        if '0'<=dart[i]<='9':
             # 10일 경우
            if dart[i] == '0' and dart[i-1]=='1':
                num[-1] = 10
            else:
                num.append(int(dart[i]))
        # S, D, T에 대한 보너스 점수
        elif dart[i] == 'S':
            continue
        elif dart[i] == 'D':
            num[-1]*=num[-1]
        elif dart[i] == 'T':
            num[-1]*=num[-1]*num[-1]
        # 아차상일 경우 점수를 마이너스한다. 
        elif dart[i] == '#':
            num[-1] *= (-1)
        # 스타상일 경우 이전 점수와 현재점수를 두배한다. 단, 처음일 경우 첫 점수만 두배한다.
        # 아차상과 중복이된다.
        elif dart[i] == '*':
            if len(num)>=2:
                num[-1] *=2
                num[-2] *=2
            else:
                num[-1] *= 2
    
    return sum(num)
