import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    cmd_type = command[0]
    
    if cmd_type == '1':
        x = int(command[1])
        dq.appendleft(x)
    elif cmd_type == '2':
        x = int(command[1])
        dq.append(x)
    elif cmd_type == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd_type == '4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd_type == '5':
        print(len(dq))
    elif cmd_type == '6':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd_type == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd_type == '8':
        if dq:
            print(dq[-1])
        else:
            print(-1)
