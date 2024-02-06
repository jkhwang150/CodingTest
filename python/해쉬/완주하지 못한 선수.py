# 효율성 통과 X
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = participant[0]
    return answer
