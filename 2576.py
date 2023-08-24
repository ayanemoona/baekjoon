num=[]
for i in range(7):
    A=int(input())
    if A%2!=0:
        num.append(A)
    else:
        continue
if len(num)==0:
    print(-1)
else:
    result=sum(num)
    print(result)
    num.sort()
    print(num[0])