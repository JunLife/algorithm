import sys

n = int(sys.stdin.readline())
_set = [0] * 21
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    
    if len(command) == 1:
        if command[0] == 'empty':
            _set = [0] * 21
        else:
            _set = [1] * 21
    else:
        if command[0] == 'add':
            _set[int(command[1])] = 1
        elif command[0] == 'remove':
            _set[int(command[1])] = 0
        elif command[0] == 'check':
            print(_set[int(command[1])])
        elif command[0] == 'toggle':
            v = int(command[1])
            if _set[v] == 1:
                _set[v] = 0
                continue
            _set[v] = 1