# 주사위 게임
# 많은 경우의 수가 나왔지만 최대한 줄여서 만들었다
s=int(input())
result=[]
for i in range(s):
    a=list(map(int,input().split()))
    if a[0]==a[1] and a[0]==a[2]:
        num=10000+(a[0]*1000)
        result.append(num)
    elif a[0]!=a[1] and a[0]!=a[2]:
        if a[1]!=a[2]:
            num=max(a)*100
            result.append(num)
        elif a[1]==a[2]:
            num=1000+(a[1]*100)
            result.append(num)
    elif a[0]==a[1] or a[0]==a[2]:
        num=1000+(a[0]*100)
        result.append(num)



print(max(result))
        