n,k=map(int,input().split())
arr=[0]+list(map(int,input().split()))
arr.append(arr[1])
prefix_sum=[0]*(n+2)
prefix_sum[0]=0
for i in range(1,n+2):
    prefix_sum[i]=prefix_sum[i-1]+arr[i]

Max=0
for i in range(n):
    if i+k<=n:
        Max = max(Max, prefix_sum[i + k] - prefix_sum[i])
    else:
        Max = max(Max, prefix_sum[n] - prefix_sum[i] + prefix_sum[(i + k) % n])

print(Max)