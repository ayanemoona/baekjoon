N=int(input())
B=0
score=0
plus=0

A=list(map(int,input().split()))
while B!=N:
    if A[B]==0:
        plus=0
        B+=1
    elif A[B]==1:
        plus+=1
        score+=plus
        B+=1
print(score)

