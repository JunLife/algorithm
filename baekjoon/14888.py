import sys

def add_op(_list, n, op):
    for _ in range(n):
        _list.append(op)

def dfs(level, now_value):
    global check, _min, _max

    if level >= n:
        _min = min(_min, now_value)
        _max = max(_max, now_value)
        return

    op_value = nums[level]
    for i in range(n - 1):
        if check[i]:
            continue
        check[i] = True
        op = op_list[i]
        if op == '//':
            if now_value < 0:
                next_value = -(abs(now_value) // op_value)
            else:
                next_value = now_value // op_value
        if op == '-':
            next_value = now_value - op_value
        if op == '*':
            next_value = now_value * op_value
        if op == '+':
            next_value = now_value + op_value
            
        dfs(level + 1, next_value)
        check[i] = False
    

if __name__ == '__main__':
    n = int(sys.stdin.readline()) # 수의 개수
    nums = list(map(int, sys.stdin.readline().strip().split())) # 정수
    op_nums = list(map(int, sys.stdin.readline().strip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
    op_list = list()
    add_op(op_list, op_nums[0], '+')
    add_op(op_list, op_nums[1], '-')
    add_op(op_list, op_nums[2], '*')
    add_op(op_list, op_nums[3], '//')
    check = [False] * (n - 1)
    
    _max = float('-inf')
    _min = float('inf')
    dfs(1, nums[0])
    
    print(_max)
    print(_min)