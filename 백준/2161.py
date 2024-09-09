#2161
N=int(input())
M=list(range(1,N+1))
delete=[]
while len(M)!=1:
    A=M.pop(0)
    delete.append(A)
    B=M.pop(0)
    M.append(B)
result=delete+M
for i in result:
    print(i,end=' ')