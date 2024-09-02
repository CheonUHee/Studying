import sys
from collections import deque

input = sys.stdin.readline

# 4방향 탐색..상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


visited = set()
# DFS 이용
stack = deque()
total_sheep = 0
total_wolf = 0

R, C = map(int, input().split())
field = [input().rstrip() for _ in range(R)]

for i in range(R):
    for j in range(C):
        if field[i][j] != '#' and (i, j) not in visited:
            # 구역의 양/늑대 마리 수 세는 변수
            sector_sheep, sector_wolf = 0, 0

            # 시작점이 양일 경우
            if field[i][j] == 'o':
                sector_sheep += 1
                stack.append((i, j))
            # 시작점이 늑대일 경우
            elif field[i][j] == 'v':
                sector_wolf += 1
                stack.append((i, j))
            # 시작점이 평지일 경우
            else:
                stack.append((i, j))
            visited.add((i, j))
            
            # 스택이 빌 때까지 작동
            while stack:
                # 방문
                r, c = stack.pop()
                

                # 탐색
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C:
                        continue
                    if (nr, nc) in visited:
                        continue
                    if field[nr][nc] != '#':
                        if field[nr][nc] == 'o':
                            sector_sheep += 1
                        if field[nr][nc] == 'v':
                            sector_wolf += 1
                        
                        stack.append((nr, nc))
                        visited.add((nr, nc))
                        

            # 한 구역의 탐색이 끝난 후, 양/늑대 마리 수 정산하기
            # 구역에서 양 마리 수가 더 많으면 전체 양 마리 수에 더하기
            if sector_sheep > sector_wolf:
                total_sheep += sector_sheep
            # 구역에서 늑대 마리 수가 같거나 더 많으면 전체 늑대 마리 수에 더하기
            else:
                total_wolf += sector_wolf
            
print(total_sheep, total_wolf)