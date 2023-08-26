

import heapq
import sys
INF = 1e10
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis = [INF]*(n+1)
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for x in graph[now]:
            cost = d + x[1] 
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, [cost, x[0]])


n=int(input())
a,b,c=map(int,input().split())
m=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d,e,w=map(int,input().split()) #d:땅1 e:땅2 w:weight
    graph[d].append((e, w))
    graph[e].append((d, w))

maxs=-INF
ans=0
totalDist = [INF for _ in range(n+1)] # total, min
for i, x in enumerate([a, b, c]):
    distance = [INF for _ in range(n+1)]
    dijkstra(x)
    for j in range(1, n+1):
        totalDist[j] = min(totalDist[j], distance[j])
result = 1
for i in range(2, n+1):
    if totalDist[result] < totalDist[i]:
        result = i
print(result)

