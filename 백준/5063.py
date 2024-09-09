s=int(input())
answer=[]
for i in range(s):
    r,e,c=map(int,input().split())
    if r+c==e:
        answer.append('does not matter')
    elif r+c<e:
        answer.append('advertise')
    elif r+c>e:
        answer.append('do not advertise')
for i in answer:
    print(i)

