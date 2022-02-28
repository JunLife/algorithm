def solution(new_id):
    answer = ''
    
    id = ''
    pre = '.'
    new_id = new_id.lower()
    for c in new_id:
        if c.isalnum() or c == '-' or c == '_' or c == '.':
            if pre == '.' and c == '.':
                continue
            pre = c
            id += c

    while id and id[-1] == '.':
        id = id[:-1]
    if id == '':
        id = 'a'
    if len(id) >= 16:
        id = id[:15]
    while id and id[-1] == '.':
        id = id[:-1]
    if len(id) <= 2:
        while len(id) < 3:
            id += id[-1]
    
    return id