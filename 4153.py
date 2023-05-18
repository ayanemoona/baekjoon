# 직각삼각형
A=[]
B=[]
while True:
    a=list(map(int,input().split()))
    
    if  0 in a:
        break
    A.append(a)
for i in range(len(A)):
    b=A[i][0]**2
    c=A[i][1]**2
    d=A[i][2]**2
    if d>b:
        if d>c:
            continue
        elif d<c:
            box=d
            d=c
            c=box
    elif d<b:
        box=d
        d=b
        b=box
        if d>c:
            continue
        elif d<c:
            box=d
            d=c
            c=box
    if b+c==d:
        B.append('right')
    else:
        B.append('wrong')
for i in B:
    print(i)    
# 