N=int(input())
A=1
B=N-1
result=[]
for i in range(N,0,-1):
    num=(' '*B)+(A*'*')
    result.append(num)
    A+=2
    B-=1
for j in range((len(result)-1),-1,-1):
    print(result[j])
