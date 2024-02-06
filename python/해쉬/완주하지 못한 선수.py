# 효율성 통과 X
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = participant[0]
    return answer

# 효율성 정확성 통과
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(0,len(completion)):
        if participant[i] == completion[i]:
            continue
        else:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]
    return answer
