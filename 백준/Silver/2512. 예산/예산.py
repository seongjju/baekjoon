
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input()) 

prefix_sum=0
for i in arr:
    prefix_sum+=i

if prefix_sum<=m:
    print(max(arr))
else:
    start,end=0,max(arr)
    while start<=end:
        total=0
        mid=(start+end)//2
        for i in arr:
            if i>mid:
                total+=mid
            else:
                total+=i
        if total<=m:
            start=mid+1
        else:
            end=mid-1
    print(end)
 