def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def lcm(A,B):
    C=(A*B)//gcd(A,B)
    return C

A,B=map(int,input().split())
    
print(lcm(A,B))
#훨씬 간단 버전