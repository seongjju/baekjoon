import sys
input = sys.stdin.readline
from collections import deque

n,m,v=map(int,input().split())

#노드 연결여부
graph=[[False]* (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True

visited1=[False]* (n+1) #dfs방문기록
visited2=[False]* (n+1) #bfs방문기록


def dfs(v): #재귀
    visited1[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if not visited1[i] and graph[v][i]: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)
def bfs(v): #큐
    q=deque([v]) #pop메서드의 시간복잡도가 O(1)로 작은 덱 내장 메서드 사용. 리스트사용시 poplast는 O(1)이지만, pop intermediate O(k)
    visited2[v] =True
    while q:
        v=q.popleft() #큐의 첫번째 값 꺼내기
        print(v,end=' ')
        for i in range(1,n+1):
            if not visited2[i] and graph[v][i]: ## 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i) #i 값(노드) 추가
                visited2[i] = True #i 값 방문 처리




dfs(v)
print()
bfs(v)
