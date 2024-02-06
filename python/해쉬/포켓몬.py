def solution(nums):
    answer = 0
    s = len(nums)//2
    lis = []
    for i in nums:
        if i not in lis:
            lis.append(i)
    if s <= len(lis):
        answer = s
    else:
        answer = len(lis)
    return answer
