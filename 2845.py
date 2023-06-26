# 숫자형 리스트 join
L,P=map(int,input().split())
num=list(map(int,input().split()))
for i in range(len(num)):
    A=L*P
    num2=num[i]-A
    num[i]=num2
result1=[str(a)for a in num]
print(" ".join(result1))