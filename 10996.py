N=int(input())
A=0
B=0
if N%2==0:
    A+=N//2
    B+=N//2
else:
    A+=N//2+1
    B+=N//2
for i in range(N):
    print('* '*A)
    print(' *'*B)