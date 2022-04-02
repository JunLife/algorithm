import sys

n = int(sys.stdin.readline().strip())
values = map(int, sys.stdin.readline().strip().split())
_sum = 0
_sum_list = list()
for value in values:
    _sum  += value
    _sum_list.append(_sum)

case_n = int(sys.stdin.readline().strip())
for i in range(case_n):
    st, ed = map(int, sys.stdin.readline().strip().split())
    st -= 2
    ed -= 1
    if st < 0:
        print(_sum_list[ed])
    else:
        print(_sum_list[ed] - _sum_list[st])