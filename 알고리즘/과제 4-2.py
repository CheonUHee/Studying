def max_items(n):
    if n == 1:
        return d[0]
    elif n == 2:
        return d[0] + d[1]

    # n >= 3일 때 계산값 저장용 dp 배열 만들기
    dp = [0] * n
    dp[0] = d[0] # n = 1
    dp[1] = d[0] + d[1] # n = 2
    dp[2] = max(d[0] + d[2], d[1] + d[2]) # n = 3

    for i in range(3, n):
        # ~(n-2)번째 + n번째 지점 or ~(n-3) + n-1번째 + n번째 지점 중
        # 최댓값 저장
        dp[i] = max(dp[i-2] + d[i], dp[i-3] + d[i-1] + d[i])

    
    return dp[n-1]


n = int(input())
d = [int(input()) for _ in range(n)]

print(max_items(n))