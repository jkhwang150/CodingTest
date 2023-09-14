def solution(new_id):
    answer = ''
    # 규칙 1. 알파벳을 모두 소문자로 치환
    new_id = new_id.lower()
    # 규칙 2. 소문자, 숫자, -, _, .를 제외한 문자 삭제
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    # 규칙 3. .가 2번 이상 연속되면 .하나로 치환
    while '..' in answer:
        answer = answer.replace('..','.')
    # 규칙 4. .이 처음이나 끝이면 삭제
    answer = answer.strip('.')
    # 규칙 5. 빈 문자열일 경우 a를 대입
    answer = 'a' if answer == '' else answer
    # 규칙 6. 길이가 16자 이상이면 15까지만 가져가고 마지막이 .이면 삭제
    if len(answer) >=16:
        answer = answer[:15]
    answer = answer.strip('.')
    # 규칙 7. 길이가 2자 이하이면 마지막 문자를 3이 될때까지 끝에 new_id를 반복해서 붙인다.
    if len(answer) <=3:
        answer = answer + answer[-1] * (3-len(answer))
        
    return answer
