import sys

t = int(sys.stdin.readline())
for _ in range(t):
    order = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    q_string = sys.stdin.readline().strip()[1:-1]
    if q_string == '':
        q = list()
    else:
        q = list(map(int, q_string.split(',')))
    status = True

    is_reversed = False
    left = 0
    right = len(q)
    for o in order:
        if o == 'R':
            is_reversed = not is_reversed
            continue
        if right - left >= 1:
            if is_reversed:
                right -= 1
            else:
                left += 1
        else:
            print('error')
            status = False
            break
    
    if status:
        q = q[left:right]
        if is_reversed:
            q = q[::-1]
        print('[', ','.join(map(str, q)), ']', sep = '')