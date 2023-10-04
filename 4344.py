#4344
answer=int(input())
for i in range(answer):
    N=list(map(int,input().split()))
    M=N.pop(0)
    count=0
    for i in N:
        if i>sum(N)/M:
            count+=1
    A=round((count/len(N))*100,3)
    print(f"{A:.3f}%")