def solution(numbers, hand):
    answer = ''
    
    mapping = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        10: (3, 0), # *
        0: (3, 1),
        12: (3, 2) # #
    }
    left_lo = 10
    right_lo = 12
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            left_lo = num
            answer += 'L'
            continue
        
        if num == 3 or num == 6 or num == 9:
            right_lo = num
            answer += 'R'
            continue
            
        target = mapping[num]
        left_now = mapping[left_lo]
        rigth_now = mapping[right_lo]
        
        left_dis = abs(target[0] - left_now[0]) + abs(target[1] - left_now[1])
        right_dis = abs(target[0] - rigth_now[0]) + abs(target[1] - rigth_now[1])
        
        if left_dis == right_dis:
            if hand == 'left':
                left_lo = num
                answer += 'L'
            else:
                right_lo = num
                answer += 'R'
            continue
        
        if left_dis > right_dis:
            right_lo = num
            answer += 'R'
        else:
            left_lo = num
            answer += 'L'
    
    return answer