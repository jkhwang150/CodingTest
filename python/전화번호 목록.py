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
def solution(phone_book):
    
    # 정렬하기 => 접두어가 되는 번호가 항상 인접한 위치에 있음
    phone_book.sort()
    
    # 현재 전화번호와 다음 전화번호를 순차 비교
    # 접두어가 있다면 False 반환
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    # 접두어가 없다면 True 반환
    return True
