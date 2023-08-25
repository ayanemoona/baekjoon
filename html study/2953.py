score=[0,0,0,0,0]
Max=score[0]
index=0
for i in range(5):
    A=list(map(int,input().split()))
    score[i]+=sum(A)
    if Max<score[i]:
        Max=score[i]
        index=i
    else:
        continue
print(index+1,Max)
