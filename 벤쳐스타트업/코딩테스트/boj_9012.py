import sys

input = sys.stdin.readline


for _ in range(int(input())):
    word = input().rstrip()
    if word[0] == ')':
        print('NO')
        continue
    
    # 스택 이용
    stack = []
    for i in word:
        # stack에 () 꼴이 나타났을 때 pop
        # 아니라면 stack에 추가    
        if i == ')':
            # stack이 비었으면 그대로 추가
            if not stack:
                stack.append(i)
            # stack이 안 비었으면 ()꼴 되는지 체크
            elif stack[-1] == '(':
                stack.pop()
        # i == '('이면 추가 
        else:
            stack.append(i)
            

    # stack이 비면 YES, 남았으면 NO 출력
    if not stack:
        print('YES')
    else:
        print('NO') 