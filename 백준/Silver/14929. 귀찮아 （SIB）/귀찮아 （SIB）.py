n=int(input())
arr=list(map(int,input().split()))

prefix_sum=[0]*n
for i in range(1,n):
    prefix_sum[i]=prefix_sum[i-1]+arr[i]

cnt=0
for i in range(n-1):

    cnt+=arr[i] * (prefix_sum[n-1] - prefix_sum[i]) 
print(cnt)