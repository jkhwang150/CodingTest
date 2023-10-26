def solution(numbers):
    answer = []
    for i in range(0,len(numbers)+1):
        count = 0
        for j in range(i,len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                break
            else:
                count += 1
            if count == len(numbers)-i:
                answer.append(-1)
    return answer
