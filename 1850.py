#최대공약수
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
a,b=map(int,input().split())

print('1'*gcd(a,b))

# 함수사용하는 곳에 리턴 값이 들어감으로 그냥 곱해도 됨
# 두자연수의 곱=최대공약수*최소공배수