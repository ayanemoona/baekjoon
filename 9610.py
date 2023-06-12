#제 4분면
#제 1사분면은 x,y 값이 둘다 양수 제2사분면은 y값만 양수 이런식으로 풀었다.
Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0
s=int(input())
for i in range(s):
    a,b=map(int,input().split())
    if a==0 or b==0:
        AXIS+=1
    elif a>0 and b >0:
        Q1+=1
    elif a<0 and b>0:
        Q2+=1
    elif a<0 and b<0:
        Q3+=1
    elif a>0 and b<0:
        Q4+=1
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("Q4:",Q4)
print("AXIS:",AXIS)