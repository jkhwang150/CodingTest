def solution(s):
    s = s.replace(' ', '')    # 공백 제거해줌
    stack = []
    
    # 문자열 각 값이 스택의 top과 같은 경우 2회 반복되는 문자(제거)
    for i in s:
        if(len(stack) == 0):
            stack.append(i)
        elif(stack[-1] == i):
            stack.pop()
        else:
            stack.append(i)
    
    
    # 길이가 0 이면 1 리턴, 아닌 경우 0 리턴
    if(len(stack) == 0):
        return 1
    else:
        return 0
