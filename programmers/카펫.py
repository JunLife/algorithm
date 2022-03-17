def solution(brown, yellow):
    answer = []
    check = [False] * (yellow + 1)
    check[0] = True
    
    for w in range(yellow, 0, -1):
        if w * 2 >= brown:
            continue
        h = yellow // w
        
        if h * 2 + w * 2 + 4 == brown and h * w == yellow:
            answer = [w + 2, h + 2]
            break

    return answer