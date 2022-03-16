from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    dis = [float('inf')] * n
    
    init_graph(graph, edge, n)

    q = deque()
    q.append(0)
    dis[0] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == float('inf'):
                q.append(i)
                dis[i] = dis[now] + 1
    
    _max = dis[0]
    for i in range(1, n):
        if _max == dis[i]:
            answer += 1
        elif _max < dis[i]:
            answer = 1
            _max = dis[i]
            
    return answer

def init_graph(graph, edge, n):
    for e in edge:
        graph[e[0] - 1].append(e[1] - 1)
        graph[e[1] - 1].append(e[0] - 1)