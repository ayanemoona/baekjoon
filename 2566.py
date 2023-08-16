result=[]
Max_index=[0,0]
Max=0
for i in range(9):
    A=list(map(int,input().split()))
    result.append(A)
    ma=max(A)
    me=A.index(ma)

    if Max<ma:
        Max=ma
        Max_index[0]=i
        Max_index[1]=me
    elif Max>=ma:
        continue
print(Max)
print(Max_index[0]+1,Max_index[1]+1)