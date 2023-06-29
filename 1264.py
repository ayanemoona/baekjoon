# 런타임 에러가 많이 걸렸던 문제
result=[]
while True:
    A=input().lower()
    sum=0
    if A=='#':
        break

    for i in 'aeiou':
        a=A.count(i)
        sum+=a
    result.append(sum)
for i in result:
    print(i) 