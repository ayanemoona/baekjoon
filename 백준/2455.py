Max=0
people=0
for i in range(4):
    A,B=map(int,input().split())
    people-=A
    people+=B
    if Max<people:
        Max=people
    else:
        continue
print(Max)