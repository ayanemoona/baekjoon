#벌집
s=int(input())
num=1
room=1
sum=1
if s==1:
    print(1)
else:
    while True:
        A=sum+(6*num)
        room+=1
        sum+=A
        num+=1
        if s<=A:
            print(room)
            break

# 주어진 예시는 다 만족 하는 거 같은데 최단 거리에서 문제가 있나?
s=int(input())
num=1
room=1
sum=6
if s==1:
    print(1)
else:
    while True:
        num=sum+num
        room+=1

        if s<=num:
            print(room)
            break
        sum+=6