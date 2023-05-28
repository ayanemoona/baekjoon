# Yangjojang of The Year  
# 실버 등급은 어려워서 내려왔는데 내 수준은 딱 이정도 인듯
s=int(input())
answer=[]
for i in range(s):
    num=int(input())
    A=[]
    B=[]
    for i in range(num):
        a,b=map(str,input().split())
        data1=a
        data2=int(b)
        A.append(data1)
        B.append(data2)
    num1=B.index(max(B))
    num2=A[num1]
    answer.append(num2)
    
for i in answer:
    print(i)
# int(리스트[0])이면 오류가 나서 변수에 넣었다