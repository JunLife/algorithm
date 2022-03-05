def solution(id_list, report, k):
    _dict = dict()
    count = dict()
    email_count = dict()
    for id in id_list:
        _dict[id] = set()
        count[id] = 0
        email_count[id] = 0
        
    for rep in report:
        ids = rep.split()
        if not ids[1] in _dict[ids[0]]:
            count[ids[1]] += 1

        _dict[ids[0]].add(ids[1])
    
    for key, value in count.items():
        if value >= k:
            for dk, dv in _dict.items():
                if key in dv:
                    email_count[dk] += 1
            
    return [value for value in email_count.values()]