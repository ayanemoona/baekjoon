x,y,w,h=map(int,input().split())
x1=w-x
y1=h-y
A=[x,y,x1,y1]
A.sort()

print(A[0])