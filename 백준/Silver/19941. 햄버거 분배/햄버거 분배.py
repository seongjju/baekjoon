
import sys
input = sys.stdin.readline



'''
문자열을 처음부터 끝까지 반복한다.
입력된 문자열에서 P를 찾는다.
P일때 거리가 k이하인 H를 앞뒤로 찾는다.
H가 없으면 다음 P로 넘어간다.
추가로 
j가 0보다 작아지면 배열 시작 전의 요소를 찾고 있다는 뜻이므로 유효하지 않고,
j가 n보다 크거나 같게 되면 배열 끝 너머의 요소를 찾고 있다는 뜻이므로 유효하지 않기에,
j의 범위를 제한해준다.

이미 선택한 H는 다시 고르지 않는다.
H와 P를 연결한만큼 개수를 더한다.
'''
n, k = map(int, input().split())
arr = list(input().rstrip())
res = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            if -1 < j < n: # 0 <= j < n 의 조건을 만족
                if arr[j] == 'H':
                    arr[j] = '-'
                    res += 1
                    break

print(res)