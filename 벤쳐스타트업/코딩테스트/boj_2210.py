import sys
from collections import deque

input = sys.stdin.readline

# 4방향 탐색..상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


field = [list(map(str, input().split())) for _ in range(5)]

# 만들어진 숫자 저장용
nums = set()
stack = deque()

for i in range(5):
    for j in range(5):
        stack.append((i, j, field[i][j]))
        
        while stack:
            # 방문
            r, c, numsum = stack.pop()
            # 6자리 숫자가 이루어졌을 때
            # nums에 저장하고 다음 단계로 넘기기
            if len(numsum) == 6:
                nums.add(numsum)
                continue

            # 탐색
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                    continue
                # 다음 좌표와 만드는 중인 숫자를 함께 stack에 저장
                stack.append((nr, nc, numsum+field[nr][nc]))
            
print(len(nums))