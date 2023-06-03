# 거스름돈 계산 쉽넹
a,b,c=map(int,input().split())
money=(a*b)-c
if money<0:
    print(0)
else:
    print(money)