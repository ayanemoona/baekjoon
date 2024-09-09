#최소공배수
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
N=int(input())
for i in range(N):
    A,B=map(int,input().split())
    C=(A*B)//gcd(A,B)
    print(C)

