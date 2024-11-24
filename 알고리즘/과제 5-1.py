R, C = map(int, input().split())
maze = [list(map(int, input())) for _ in range(C)]

# 4방향 탐색(동,서,남,북)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

answer = 0

# DFS 이용
def DFS(r, c):
    global answer
    
    # 도착지점에 도달 시
    if r == R-1 and c == C-1:
        answer += 1
        return
    # 방문
    maze[r][c] = 1
    
    # 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if maze[nr][nc] == 1:
            continue

        # 도착지점이 아닐 시
        if maze[nr][nc] == 0:
            DFS(nr, nc)
    
    # 방문 초기화
    maze[r][c] = 0

# 시작점에서 시작     
DFS(0, 0)

print(answer)