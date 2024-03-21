def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
  
    for idx in range(1, len(words)):
      # 끝단어와 다음 시작 단어가 같은지 검사
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
      # 중복 단어 검사
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer
