n = int(input())
candies = input().split()


def dp_candies(n, candies):
    # DP 테이블
    # 이때 dp[x][y] = t는 x번째~y번째 사탕 모음에서 
    # 사탕을 파괴하는 데 걸리는 시간 t를 뜻함
    dp = [[99999] * n for _ in range(n)] # 최소 시간으로 갱신하기 위해 큰값으로 초기화
    
    # 사탕이 1개일 경우 무조건 1초 걸림
    for i in range(n):
        dp[i][i] = 1
    
    # 사탕이 2개 이상일 경우
    for length in range(2, n+1):  # 일부 구간의 길이 선택
        for i in range(n - length + 1):
            j = i + length - 1
            
            # [i:j] 양 끝이 같을 경우
            if candies[i] == candies[j]:
                # 사탕이 3개 이상이면
                # 양 끝 제외한 내부의 사탕 파괴 시간으로 임시 갱신 
                if length > 2:
                    dp[i][j] = dp[i+1][j-1]
                # 사탕이 2개이면 팰린드롬이므로 1초
                else:
                    dp[i][j] = 1
            
            # 전체 사탕을 두 부분으로 나누어
            # 사탕 최소 파괴 시간을 최종 갱신
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
    
    # 전체 사탕에 대한 최소 파괴 시간 return 
    return print(dp[0][n-1])


dp_candies(n, candies)