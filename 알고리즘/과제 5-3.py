n = int(input())
dayprice = list(map(int, input().split()))
maxprice = 0 # 고점 가격 갱신용
result = 0 # 결과값

# 고점 가격보다 낮을 때는 매수하고, 고점일 때 매도하므로
# 가격을 역순으로 체크하여
# 고점일 때는 고점 가격 갱신으로 행동을 끝내고,
# 저점일 때는 고점 가격과의 차를 result에 갱신하기
for i in range(n-1, -1, -1):
    if dayprice[i] > maxprice:
        maxprice = dayprice[i]
    else:
        result += (maxprice - dayprice[i])

print(result)