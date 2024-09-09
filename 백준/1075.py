N=list(map(int,input()))
F=int(input())
N[-1]=0
N[-2]=0
N=int(''.join(map(str,N)))
if N%F!=0:
    num=(N//F)+1
else:
    num=N//F
result=F*num
A=list(map(int,str(result)))
B=[A[-2],A[-1]]
C=''.join(map(str,B))
print(C)