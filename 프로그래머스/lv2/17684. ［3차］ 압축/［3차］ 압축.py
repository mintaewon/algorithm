def solution(msg):
#     answer = []
#     ls = ['start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     word = ""
#     for i in range(len(msg)):
#         word += msg[i]
#         if word in ls:
#             before_word = word
#         else:
#             answer.append(ls.index(before_word))
#             ls.append(word)
#             word = "" + msg[i]
#             before_word = word
            
#     answer.append(ls.index(word))
#     return answer
    answer = []
    dictionary = {chr(i+64):i for i in range(1, 27)}
    num = 27
    start = 0
    temp = ""
    while (len(msg)-1) >= start:
        temp+=msg[start]
        try:
            if dictionary[temp]:
                start+=1
                before = temp
        except:
            dictionary[temp] = num
            answer.append(dictionary[before])
            num += 1
            temp = ""
    answer.append(dictionary[before])
    return answer