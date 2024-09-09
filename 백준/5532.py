L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
a=A//C
if A%C >0:
    a+=1
b=B//D
if A%C >0:
    b+=1
if a>=b:
    result=L-a
elif a<b:
    result=L-b
print(result)