import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))
                
N, M = int(input()), int(input())
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
s, e = map(int, input().split())
dijkstra(s)
print(dis[e])