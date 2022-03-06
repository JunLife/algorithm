def solution(number, k):
    count = 0
    i = 0
    while True:
        if count >= k or i >= len(number) - 1:
            break
            
        if number[i] == '9':
            i += 1
            continue
            
        if number[i] < number[i + 1]:
            number = number[0:i] + number[i + 1:]
            count += 1
            if i < 2:
                i = 0
            else:
                i -= 2
        else:
            i += 1

    if count < k:
        number = number[0:count - k]
        
    return number