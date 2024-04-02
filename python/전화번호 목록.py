# 시간 초과 실패
# 원인 : phone_book을 두 번 순회하여 진행
def solution(phone_book):
    answer = True
    for i in phone_book:
        count = 0
        a = len(i)
        for j in phone_book:
            if i == j[:a]:
                count += 1
        if count == 1:
            continue
        else:
            return False                
    return True

# startswitch => 접두어를 찾는 함수
def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
