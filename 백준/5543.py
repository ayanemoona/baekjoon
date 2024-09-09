# 세트메뉴
# 같았을 때 조건이 조용히 들어있었다
a=int(input())
b=int(input())
c=int(input())
coke=int(input())
saida=int(input())
sum=0

if a<=b and a<=c:
    sum+=a
elif b<=a and b<=c:
    sum+=b
elif c<=a and c<=b:
    sum+=c
if coke>=saida:
    sum+=saida
elif coke<=saida:
    sum+=coke
print(sum-50)