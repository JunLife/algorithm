import sys

n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().rstrip().split()))

x_set = set(x_list)
unique_x_list = sorted(list(x_set))

compressed_x_value = dict()
for index, value in enumerate(unique_x_list):
    compressed_x_value[value] = index

for x in x_list:
    print(compressed_x_value[x], end = ' ')