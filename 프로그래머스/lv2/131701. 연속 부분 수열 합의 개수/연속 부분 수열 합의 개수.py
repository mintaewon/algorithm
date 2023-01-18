from itertools import combinations
def solution(elements):
    answer = set(elements)
    elements2 = elements*2
    for i in range(2, len(elements)+1):
        for start in range(len(elements2)):
            # print(start, i, elements2[start:start+i])
            answer.add(sum(elements2[start:start+i]))
    # print(list(answer))
    return len(answer)