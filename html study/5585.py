N=int(input())
result=0
coin=1000-N
if coin //100!=0:
    A=coin//100
    B=A//5
    C=A%5
    result+=B+C

if coin //10!=0:
    A=(coin%100)//10
    B=A//5
    C=A%5
    result+=B+C

if coin%10!=0:
    A=(coin%100)%10
    B=A//5
    C=A%5
    result+=B+C
print(result)

