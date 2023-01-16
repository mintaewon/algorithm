from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    ls = sorted(Counter(tangerine).values(), reverse=True)
    for i in range(len(ls)):
        total += ls[i]
        answer +=1
        if total >= k:
            return answer