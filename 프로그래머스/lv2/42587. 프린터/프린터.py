from collections import deque
def solution(priorities, location):
    important_ls = deque(sorted(priorities, reverse=True))
    priorities_Q = deque(priorities)
    cnt = 1
    while True:
        if important_ls[0] == priorities_Q[0]:
            if location == 0:
                return cnt
            else:
                cnt+=1
                location-=1
                important_ls.popleft()
                priorities_Q.popleft()
        else:
            if location == 0:
                priorities_Q.append(priorities_Q.popleft())
                location = len(priorities_Q)-1
            else:
                location -= 1
                priorities_Q.append(priorities_Q.popleft())
    # answer = 0
    # return answer
# 2 1`3`2
# 3 2 2 1