N=int(input())
A=list(map(int,input().split()))
B=[]
A.sort()
C=A[0]
B.append(C)
for i in range(len(A)):
    if C==A[i]:
        continue
    else:
        C=A[i]
        B.append(C)
B_1=[str(a)for a in B]
print(" ".join(B_1))