N, L, W, H = map(int, input().split())
s, e = 0, max(L, W, H)
for _ in range(100):
    m = (s+e)/2
    l=L//m
    w=W//m
    h=H//m
    if l*w*h >= N:
        s = m
    else:
        e = m
print("%.10f" %(e))