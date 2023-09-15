N=int(input())
alist=[]
for i in range(N):
    A=list(map(str,input().split()))
    alist.append(A)
for i in range(N):
    alist[i][0]=int(alist[i][0])
alist.sort(key=lambda x:x[0])

for x,y in alist:
    print(x,y)
