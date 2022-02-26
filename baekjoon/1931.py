import sys

n = int(sys.stdin.readline())

_list = list()
for i in range(n):
    s_time, e_time = map(int, sys.stdin.readline().split())
    _list.append((s_time, e_time))
    
_list.sort(key = lambda meeting : (meeting[1], meeting[0]))

result = list()
pre_end = 0
for meeting in _list:
    if meeting[0] >= pre_end:
        pre_end = meeting[1]
        result.append(meeting)

print(len(result))