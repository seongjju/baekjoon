import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
v=int(input())

graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): 
    a,b=map(int,input().split())
    graph[a]+=[b] 
    graph[b]+=[a] 

visited[1]=1 
Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)
