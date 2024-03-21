def solution(progresses, speeds):
    answer = [1]
    leave = []
    # 남은 진도
    for i in progresses:
        leave.append(100-i)
        
    # 필요한 일 수 
    days = []
    for i in range(0,len(leave)):
        if leave[i] % speeds[i] == 0:
            days.append(leave[i]//speeds[i])
        else:
            days.append(leave[i]//speeds[i]+1)
    # 필요일수가 앞 수보다 크면 리스트에 추가 / 앞 수보다 적다면 + 1
    a = 0
    for i in range(1,len(days)):
        if days[i] <= days[i-1]:
            answer[a] = answer[a] + 1
            # 비교 후 큰 수를 뒤로 보내서 더 큰수가 나올때까지 비교 진행
            days[i], days[i-1] = days[i-1], days[i]
        else:
            answer.append(1)
            a+=1
            
    return answer

