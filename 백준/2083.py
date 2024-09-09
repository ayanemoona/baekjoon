result=[]
while True:
    A=list(map(str,input().split()))
    A[1]=int(A[1])
    A[2]=int(A[2])
    if A[0]=='#'and A[1]==0 and A[2]==0:
        break
    if A[1]>17 or A[2]>=80:
        B=A[0]+' Senior'
        result.append(B)
    else:
        B=A[0]+' Junior'
        result.append(B)
for i in result:
    print(i)