import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#number of node and edge
n,m = map(int,input().split())

#start node
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#input edge info
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q: #queue is not empty
        dist,now = heapq.heappop(q)

        #이미 처리가 된 노드라면
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])
