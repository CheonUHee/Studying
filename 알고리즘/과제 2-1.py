a, b = map(int, input().split())
stack = [b, a]

# stack이 빌 때까지 실행
while stack:
    n = stack.pop()
    # n이 b를 초과할 경우 break
    if n > b:
        break
    print(n, end=' ')

    # 짝수일 때
    if n % 2 == 0:
        n += 3
        stack.append(n)
    # 홀수일 때
    elif n % 2 == 1:
        n *= 2
        stack.append(n)