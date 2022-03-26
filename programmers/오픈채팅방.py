def solution(record):
    answers = list()
    members = dict()
        
    for e in record:
        to_do = e.split()
        
        if to_do[0] == 'Enter': # 입장
            members[to_do[1]] = to_do[2]
            answers.append([to_do[1], f'{to_do[1]}님이 들어왔습니다.'])
        elif to_do[0] == 'Leave': # 퇴장
            answers.append([to_do[1], f'{to_do[1]}님이 나갔습니다.'])
        else: # 변경
            members[to_do[1]] = to_do[2]
    
    for answer in answers:
        answer[1] = answer[1].replace(answer[0], members[answer[0]])

    return list(map(lambda x : x[1], answers))