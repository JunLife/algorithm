def solution(answers):
    result = [0, 0, 0]
    
    givers_answers = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for i in range(len(answers)):
        n_giver1 = i % len(givers_answers[0])
        n_giver2 = i % len(givers_answers[1])
        n_giver3 = i % len(givers_answers[2])
        
        if answers[i] == givers_answers[0][n_giver1]:
            result[0] += 1
            
        if answers[i] == givers_answers[1][n_giver2]:
            result[1] += 1
            
        if answers[i] == givers_answers[2][n_giver3]:
            result[2] += 1

    max = float('-inf')
    output = list()

    for i, v in enumerate(result):
        if max < v:
            output = [i + 1]
            max = v
        elif max == v:
            output.append(i + 1)
    
    return output