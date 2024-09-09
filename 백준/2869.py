# 달팽이는 올라가고 싶다
day=0
sum=0
a,b,c=map(int,input().split())
while True:
    sum+=a
    day+=1
    if sum>=c:
        print(day)
        break
    sum-=b
# 큰 숫자가 나오면 시간초과 뜸
# 규칙 찾아야 하는디
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)