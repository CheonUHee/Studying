n = int(input())
fibo = [0, 1] # 피보나치 수열 계산값을 저장할 공간

for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n])