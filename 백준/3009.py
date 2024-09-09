row=[]
column=[]
answer=[]
for i in range(3):
    a,b=map(int,input().split())
    row.append(a)
    column.append(b)
for i in range(3):
    if row.count(row[i])==2:
        continue
    else:
        answer.append(row[i])
for i in range(3):
    if column.count(column[i])==2:
        continue
    else:
        answer.append(column[i])

    

for i in answer:
    print(i,end=" ")