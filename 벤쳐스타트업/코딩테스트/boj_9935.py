import sys

input = sys.stdin.readline

word = input().rstrip()
bomb = list(input().rstrip())

# 스택 이용
stack = []
for i in word:
    stack.append(i)
    
    # i가 bomb 단어의 끝 문자열일 경우
    # stack 끝부분에서 bomb 단어가 성립되는지 체크
    if (i == bomb[-1]) & (stack[-len(bomb):] == bomb[:]):
        # 성립하면 bomb 길이만큼 pop하기
        for _ in range(len(bomb)):
            stack.pop()

# stack이 비어있지 않을 경우
# stack에 들어있는 문자열을 합하여 출력
if stack:
    print(''.join(stack))
# stack이 비었을 경우
else:
    print('FRULA')

#############
## 메모리 초과한 코드
# import sys

# input = sys.stdin.readline

# def boomboom(word, bomb):
#     boom = word.split(bomb)
#     new_word = ''
    
#     for i in boom:
#         new_word += i
    
#     if bomb in new_word:
#         return boomboom(new_word, bomb)
#     else:
#         return new_word


# word = input().rstrip()
# bomb = input().rstrip()

# ans = boomboom(word, bomb)
# if ans:
#     print(ans)
# else:
#     print('FRULA')