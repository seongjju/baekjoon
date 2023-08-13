import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
for _ in range(n):
    dq = deque()
    size=int(input())
    arr=list(input().split())
    dq.append(arr[0])
    for i in range(1,len(arr)):
        if dq[0]>=arr[i]:
            dq.appendleft(arr[i])
        else:
            dq.append(arr[i])
    print("".join(dq))