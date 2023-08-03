

n=int(input())
arr=[0]+list(map(int,input().split()))
m=int(input())
li=[
    list(map(int,input().split()))
    for _ in range(m)
]
prefix_sum=[0]*((n+1))
for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+arr[i]

def get_sum(i,j):
    return prefix_sum[j]-prefix_sum[i-1]

for i in range(m):
    ans=0
    tp=li[i]
    ans=get_sum(tp[0],tp[1])
    print(ans)