import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().split())

# 초기값 입력// 0은 동생을 찾기까지 걸린 시간
queue = deque([(N, 0)])
visited = set()

# BFS 이용
while True:
    # 방문
    x, cnt = queue.popleft()
    visited.add(x)

    # x가 K에 도달하면 break
    if x == K:
        break

    # 3가지 탐색
    a, b, c = x-1, x+1, 2*x
    # 각 경우가 방문한 적이 없고, 0~100,000 범위에 존재하면
    # 큐에 추가하기
    if a not in visited and 0 <= a <= 100000:
        queue.append((a, cnt+1))
    if b not in visited and 0 <= b <= 100000:
        queue.append((b, cnt+1))
    if c not in visited and 0 <= c <= 100000: 
        queue.append((c, cnt+1))
    
print(cnt)