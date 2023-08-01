def binary_search(arr, target, start, end, cnt):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return cnt.get(target)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1, cnt)
    else:
        return binary_search(arr, target, mid + 1, end, cnt)

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

cnt = {}
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    print(binary_search(a, i, 0, len(a) - 1, cnt), end=' ')
