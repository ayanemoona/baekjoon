A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
result=0
if A<0:
    result+=C*(0-A)
    result+=D
    result+=B*E
elif A==0:
    result+=D
    result+=B*E
elif A>0:

    result+=(B-A)*E

print(result)

# 더 줄일 수 있었다