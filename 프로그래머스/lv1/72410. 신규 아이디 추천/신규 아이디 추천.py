import re

def solution(new_id):
    # 1 step
    new_id = new_id.lower()
    # 2 step
    new_id = re.sub("[~|!|@|#|$|%|^|&|*|\(|\)|=|+|\[|\{|\]|\}|:|?|,|<|>|/]", "", new_id)
    # 3 step
    new_id = re.sub("[.]+",".", new_id)
    # 4 step
    if new_id[0] == ".":
        new_id = new_id[1:]
    # 5 step
    if len(new_id) == 0:
        new_id = "a"
    # 6 step
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    # 7 step
    if len(new_id) < 3:
        new_id = new_id.ljust(3, new_id[-1])
    
    return new_id