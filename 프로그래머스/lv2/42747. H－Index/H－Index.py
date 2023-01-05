def solution(citations):
    answer = 0
    ls = sorted(citations, reverse=True)
    maximum = ls[0]
    minimum = ls[-1]
    for h in range(maximum, -1, -1):
        result = list(filter(lambda x: x>=h, ls))
        if h <= len(result):
            answer = h
            break
    return answer