import sys

n, m = map(int, sys.stdin.readline().split()) # 저장된 사이트 주소의 수, 찾으려는 사이트 주소의 수
_list = [list(sys.stdin.readline().split()) for _ in range(n)]
target_list = [sys.stdin.readline().rstrip() for _ in range(m)]
result = list()
_dict = dict(_list)

for i in range(m):
    result.append(_dict[target_list[i]])

print('\n'.join(result))