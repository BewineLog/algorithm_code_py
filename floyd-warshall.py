import sys
INF = int(1e9)

# node,edge 갯수
n,m = map(int,input().split())

graph = [[INF] * (n + 1) for i in range(n+1)]

# 자기 자신으로 향하는 cost = 0
for i in range(1,n+1):
    graph[i][i] = 0

# edge에 대한 정보 입력받기 a->b :cost c
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1,n+1):  # 경유 point
    for a in range(1,n+1):  # start point
        for b in range(1,n+1):  # end point
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('infinite',end=' ')
        else:
            print(graph[a][b], end=' ')
    print()