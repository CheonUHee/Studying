# 백준 1992번과 같음
import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().rstrip())) for _ in range(N)]


def QuadTree(N, row, column): # (행렬 사이즈, 행 시작점, 열 시작점)
    # flag 변수
    onlyOne = True
    onlyZero = True

    for r in range(row, row + N):
        for c in range(column, column + N):
            if maps[r][c] == 1:
                onlyZero = False
            else:
                onlyOne = False
            
            # onlyOne과 onlyZero가 둘다 Fasle일 경우
            # 즉시 4분할 실행
            if not onlyOne and not onlyZero:
                # 제 2 사분면, 제 1 사분면, 제 3 사분면, 제 4 사분면 순서
                print('(', end='')
                QuadTree(N//2, row, column)
                QuadTree(N//2, row, column + N//2)
                QuadTree(N//2, row + N//2, column)
                QuadTree(N//2, row + N//2, column + N//2)
                print(')', end='')
                return
    # 해당 행렬(혹은 분할된 행렬)에 0 또는 1만 존재할 경우 출력
    if onlyOne:
        print(1, end='')
    elif onlyZero:
        print(0, end='')
        
QuadTree(N, 0, 0)