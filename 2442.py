N=int(input())
A='*'
B=N-1
for i in range(1,N+1):
    no=' '*B
    print(no+A)
    A+='**'
    B-=1
    
    