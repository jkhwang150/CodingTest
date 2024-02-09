def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            row = int(yellow/i)
            col = i
            if((2*(row+col)+4) == brown):
                return [row+2,col++2]
  
