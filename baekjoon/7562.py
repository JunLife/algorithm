import sys
from collections import deque

if __name__ == '__main__':
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        board_len = int(sys.stdin.readline())
        st_y, st_x = map(int, sys.stdin.readline().strip().split())
        target_y, target_x = map(int, sys.stdin.readline().strip().split())
        
        board = [[0] * board_len for _ in range(board_len)]
        q = deque()
        q.append((st_y, st_x))
        
        while q:
            now = q.popleft()
            now_y = now[0]
            now_x = now[1]
            if now_y == target_y and now_x == target_x:
                break
            
            for i in range(8):
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]
                if 0 <= next_x < board_len and 0 <= next_y < board_len and board[next_y][next_x] == 0:
                    board[next_y][next_x] = board[now_y][now_x] + 1
                    q.append((next_y, next_x))
                    
        print(board[target_y][target_x])