import sys

input = sys.stdin.readline
# 파이썬이 정한 최대 재귀 깊이 변경하기(기본 1,000 -> 1백만으로 변경)
sys.setrecursionlimit(10**6)

# 4방향 탐색..상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS():
    # 방문
    r, c = stack.pop()

    # 탐색
    for d in range(4):
        nr, nc = r + dr[d], c+dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if (nr, nc) in visited:
            continue

        if field[nr][nc] == 1:
            stack.append((nr, nc))
            visited.add((nr, nc))
            # 다시 DFS 함수 실행(재귀)
            DFS()



for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]

    #방문지 기록
    visited = set()
    stack = []
    # 지렁이 마리 수 세는 변수
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        # 배추가 존재하는 칸 = 1
        field[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if (i, j) not in visited and field[i][j] == 1:
                stack.append((i, j))
                visited.add((i, j))
                DFS()
                cnt += 1
    
    print(cnt)