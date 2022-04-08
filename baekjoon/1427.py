import sys

s = sys.stdin.readline().strip()
num_list = list(s)
num_list.sort(reverse = True)
print(''.join(num_list))