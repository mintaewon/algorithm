from collections import deque
def solution(people, limit):
    answer = 0
    sp = sorted(people, reverse=True)
    end = len(sp)-1
    temp = 0
    for start in range(len(sp)):
        temp = sp[start]
        while start <= end:
            if temp+sp[end] <= limit:
                answer +=1
                end-=1
                break
            else:
                answer += 1
                break
    return answer