A=input()

if int(A)>=100:
    if A[-2]=='1' and A[-1]=='0':
        B2=A[:-2]
        B3=A[-2:]
    else:
        B2=A[-1]
        B3=A[0:-1]
    print(int(B2)+int(B3))
else:
    B2=A[0]
    B3=A[1]
    print(int(B2)+int(B3))

## 숨켜진 조건까지 완벽하게 해결