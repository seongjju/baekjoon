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
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))
    return dis

n=int(input())
a,b,c=map(int,input().split())
m=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d,e,w=map(int,input().split()) #d:땅1 e:땅2 w:weight
    graph[d].append((e, w))
    graph[e].append((d, w))

dis_a = dijkstra(a)
dis_b = dijkstra(b)
dis_c = dijkstra(c)

max_distance = -INF
answer = 0

for i in range(1, n+1):
    min_distance = min(dis_a[i], dis_b[i], dis_c[i])
    if min_distance > max_distance:
        max_distance = min_distance
        answer = i

print(answer)
