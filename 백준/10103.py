# 주사위 놀이
player1=100
player2=100
s=int(input())
for i in range(s):
    a,b=map(int,input().split())
    if a==b:
        continue
    elif a>b:
        player2-=a
    elif a<b:
        player1-=b
print(player1)
print(player2)