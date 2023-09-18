N=int(input())
A=[]
B=[]
for i in range(N):
    x,y=map(int,input().split())
    A.append([x,y])

for x,y in A:
    score=0
    for a,b in A:
        if x<a and y<b:
            score+=1
    B.append(score+1)
B_str=[str(a)for a in B]
print(' '.join(B_str))

