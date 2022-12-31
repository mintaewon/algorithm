def func(dic, x):
    if dic[x[0]] > dic[x[1]]:
        return x[0]
    elif dic[x[0]] < dic[x[1]]:
        return x[1]
    else:
        return x[0]

def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0, 'C':0, 'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] < 4:
            dic[survey[i][0]] += (4-choices[i])
        elif choices[i] > 4:
            dic[survey[i][1]] += (choices[i]-4)
    
    for s in ['RT', 'CF', 'JM', 'AN']:
        answer += func(dic, s)
    return answer