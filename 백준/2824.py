def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
def multiply(lst):
    return eval('*'.join(str(x) for x in lst))

def digitize (n):
    return list(map(int,str(n)))

N=int(input())
a=list(map(int,input().split()))
if N==len(a):
    A=multiply(a)
M=int(input())
b=list(map(int,input().split()))
if M==len(b):
    B=multiply(b)
result=gcd(A,B)
C=digitize(result)
if len(C)>9:
    for i in range((len(C)-9),len(C)):
        print(C[i],end='')
else:
    for i in range(len(C)):
        print(C[i],end='')

# 함수사용 함!
# 리스트는 곱셈 불가능하구나!
#뿌듯