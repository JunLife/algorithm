import sys

def d_q(y, x, n, result):
    bound = n // 3
    
    paper = get_paper(y, x, n)
    if paper == None:
        result = d_q(y, x, bound, result)
        result = d_q(y + bound, x, bound, result)
        result = d_q(y + bound * 2, x, bound, result)
        result = d_q(y, x + bound, bound, result)
        result = d_q(y + bound, x + bound, bound, result)
        result = d_q(y + bound * 2, x + bound, bound, result)
        result = d_q(y, x + bound * 2, bound, result)
        result = d_q(y + bound, x + bound * 2, bound, result)
        result = d_q(y + bound * 2, x + bound * 2, bound, result)
    else:
        result[paper] += 1
    
    return result

def get_paper(y, x, n):
    pre = board[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if pre != board[i][j]:
                return None
    return pre

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    board = [sys.stdin.readline().strip().split() for _ in range(n)]
    
    result = d_q(0, 0, n, {'-1': 0, '0': 0, '1': 0})
    print(result['-1'])
    print(result['0'])
    print(result['1'])