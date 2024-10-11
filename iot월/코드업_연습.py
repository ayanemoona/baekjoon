a=int(input())
lst=[]
rang=[1]*a
for i in range(a):
    b=int(int(input()))
    lst.append(b)
for i in range(a):
    for j in range(a):
        if i==j :
            continue
        elif lst[i]<lst[j]:
            rang[i]+=1
for i in rang:
    print(i)