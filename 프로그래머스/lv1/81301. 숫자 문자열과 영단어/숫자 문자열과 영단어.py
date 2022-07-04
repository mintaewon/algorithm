def solution(s):
    
    en_ls = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(en_ls)):
        if en_ls[i] in s:
            s = s.replace(en_ls[i], str(i))
    return int(s)