# 2016년
def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    return day[(sum(mon[:a-1]) + b) % 7]

# 문자열 내림차순으로 배치하기
def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    lis = "".join(arr)
    return lis.

# 문자열 다루기 기본
def solution(s):
    return s.isdigit() and len(s) in(4,6)
