from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
    command = input().strip()
    if command.startswith('push'):
        x = int(command.split()[1])
        x=int(x)
        q.append(x)
    elif command=='pop':
        if len(q)==0:
            print(-1)
        else:    
            print(q.popleft())

    elif command=='size':
        print(len(q))
    elif command=='empty':
        if len(q)==0:
            print(1)
        else:    
            print(0)
    elif command=='front':
        if len(q)==0:
            print(-1)
        else:    
            print(q[0])
    elif command=='back':
        if len(q)==0:
            print(-1)
        else:    
            print(q[-1])


