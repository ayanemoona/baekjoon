# 5월 16일
# ACM 호텔 
s=int(input())
num=[]
D=[]
for i in range(s):
    a1=list(map(int,input().split()))
    num.append(a1)
    #층수
    A=num[i][2]%num[i][0]
    A1=str(A)
    B=num[i][2]//num[i][0]
    if B<10:
        B1='0'+str(B+1)
    else:
        B1=str(B+1)
    C=A1+B1
    D.append(C)
for i in D:
    print(i)

'''
처음에는 모든 호텔의 호수를 다 구한뒤 위치를 이동하는 걸로 할라고 하였으나 구현하다 빡세서 바꿈
문제에서 틀렸다고 함 =>? 나머지가 0일때를 구현 안해서
'''
s=int(input())

for i in range(s):
    a,b,c=map(int,input().split())
    #층수
    A=c%a
    B=c//a+1
    if A==0:
        A=a
        B-=1
    print(A*100+B)