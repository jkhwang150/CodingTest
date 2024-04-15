def solution(s, skip, index):
    answer = ''
    alphabet = ''
    # 모든 알파벳 소문자 추가
    for i in range(ord('a'),ord('z')+1):
        alphabet += chr(i)
    # skip에 있는 문자 제거
    for sk in skip:
        alphabet = alphabet.replace(sk, '')
    # 인덱스만큼 이동
    # 만약 'z'를 넘어간다면 다시 앞에서부터 순환
    for a in s:
        idx = (alphabet.index(a) + index ) % len(alphabet)
        answer += alphabet[idx]
    
    return answer
