# 이렇게 짰는데 틀림 더 쉬운 방법도 있었음
a,b,c=map(int,input().split())
cooking=int(input())
if cooking//60 <60:
    num=cooking//60
    b+=num
    num2=cooking%60
    c+=num2
elif cooking//60 >=60:
    num=cooking//60
    num0=num//60
    a+=num0
    num2=num%60
    b+=num2
    num3=cooking%60
    c+=num3   
# 생각해보니 같은거 반복한거 아닌가? 더 복잡하게 하고 있었네

if c==60:
    c=0
    b+=1 
elif c>60:
    C=c//60
    c=c%60
    b+=C
if b==60:
    b=0
    a+=1
elif b>60:
    B=b//60
    b=b%60
    a+=B
if a==24:
    a=0
elif a>24:
    a=a//24
print(a,b,c)

# 인터넷 답 나눗셈 이용
a,b,c=map(int,input().split())
cooking=int(input())
c+=cooking
b+=c//60
a+=b//60
print(a%24,b%60,c%60)
