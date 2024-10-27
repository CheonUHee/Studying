word = input()
Letter = []

# 아스키 코드를 기반으로 알파벳만 남기기
for i in word:
    # 아스키 코드가 A보다 작거나, z보다 크거나, Z ~ a 사이에 있는 것은 제외
    if ord(i) < ord('A') or ord(i) > ord('z') or ord('Z') < ord(i) < ord('a'):
        continue
    Letter.append(i)
print(len(Letter))