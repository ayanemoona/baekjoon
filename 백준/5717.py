#상근이의 친구들
#난이도: 하
people=[]
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    people.append(a+b)
for i in people:
    print(i)