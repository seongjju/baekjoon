

def get_sum(i,j,x,y):
    return prefix_sum[x][y]-prefix_sum[i-1][y]-prefix_sum[x][j-1]+prefix_sum[i-1][j-1]

n,m=map(int,input().split())
arr = [[0]*(m+1)]+[
    [0]+list(map(int,input().split()))
    for _ in range(n)
]

prefix_sum =[
    [0]*(m+1)
    for _ in range(n+1)
]

prefix_sum[0][0]=0
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+arr[i][j]
k=int(input())
tupple =  [[0]*(5)]+[
    [0]+list(map(int,input().split()))
    for _ in range(k)

]

for i in range(1,k+1):
    ans=0
    tp = tupple[i]
    ans = get_sum( tp[1], tp[2], tp[3],tp[4])
    print(ans)