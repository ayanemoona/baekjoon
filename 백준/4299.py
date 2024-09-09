A,B=map(int,input().split())
C=(A+B)//2
D=A-C
if A+B<0 or A-B<0 or (A+B)%2!=0:
    print(-1)
else:
    C=(A+B)//2
    D=A-C   
    print(max(C,D),min(C,D))