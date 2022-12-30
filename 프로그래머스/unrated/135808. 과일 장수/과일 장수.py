def solution(k, m, score):
    answer = 0
    n_score = sorted(score, reverse=True)
    for i in range(0,len(n_score), m):
        temp = n_score[i:i+m]
        if len(temp) == m:
            answer += min(temp)*m
    return answer