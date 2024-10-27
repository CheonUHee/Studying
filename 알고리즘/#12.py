# 행과 열
N, M = map(int, input().split())

# 매트릭스 요소 값 받기
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 반복문으로 행 뽑아서 더하기
for row in matrix:
    tmp = sum(row)
    ans += tmp

print(ans)