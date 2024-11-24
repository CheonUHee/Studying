string1 = input().rstrip() 
string2 = input().rstrip() 

n = len(string1) # 행 역할
m = len(string2) # 열 역할

# 2차원 배열을 만들고, string1과 string2의 각 문자를 하나씩 비교하여
# Longest Common Sequence(LCS)를 만족할 때마다 결과값을 배열에 저장하기

LCS = [[0] * (m+1) for _ in range(n+1)] # 0으로 초기화

# 행,열의 인덱스 0은 LCS 탐색 연산을 위해 비워두기
for r in range(1, n+1):
    for c in range(1, m+1):
        # 문자가 같으면, 해당 문자가 두 문자열에 추가되기 전의 결과값에 +1
        if string1[r-1] == string2[c-1]:
            LCS[r][c] = LCS[r-1][c-1] + 1
        # 문자가 다르면, 직전까지의 LCS 결과값은 유지되므로
        # 이때의 갱신 값을 LCS[r-1][c], LCS[r][c-1] 중 최댓값으로 갱신함
        else:
            LCS[r][c] = max(LCS[r-1][c], LCS[r][c-1])

print(LCS[n][m])