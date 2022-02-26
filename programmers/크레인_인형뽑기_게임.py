def solution(board, moves):
    answer = 0
    basket = list()
    
    for move in moves:
        for i in range(len(board)):
            target = board[i][move - 1]
            if target == 0:
                continue
            
            board[i][move - 1] = 0
            if basket and target == basket[-1]:
                answer += 2
                basket.pop()
            else:
                basket.append(target)
            break
    return answer