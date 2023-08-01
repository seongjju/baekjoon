N, L = map(int, input().split())
pos = 0 #현재 위치
answer = 0 #경과 시간
for _ in range(N):
    d, r, g = map(int, input().split())

#경과시간=신호등 위치 - 현재위치
    answer += (d - pos)
#현재위치 갱신
    pos = d
#빨간불+초록불을 경과시간에 나눈 나머지가 빨간불 이하이면 대기
#대기시간만큼 경과시간에 더함
    if answer % (r+g) <= r:
        answer += (r - (answer%(r+g)))
#n개 신호 입력받은 후 마지막 신호등과 l과의 거리를 경과 시간에 더하고 출력
answer += (L-pos)
print(answer)