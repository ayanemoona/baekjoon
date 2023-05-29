#화성수학
s=int(input())
answer=[]
for i in range(s):
    a=list(map(str,input().split()))
    num=float(a[0])
    score=a[1:]
    for i in score:
        if i=="@":
            num=num*3
        elif i == "%":
            num=num+5
        elif i == "#":
            num=num-7
    answer.append(num)


for i in answer:
    print("%.2f"%i)
