def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
      # or 연산자를 활용하여 2진수 값을 num에 저장
        num = bin(arr1[i] | arr2[i])
      # 2의 n승 자리수의 수로 만들어 주어야 하기에 앞을 0으로 채움
        num = num[2:].zfill(n)
      # 1은 #으로 0은 공백으로 치환하여 answer에 추가
        num = num.replace('1', '#').replace('0', ' ')
        answer.append(num)
    return answer
