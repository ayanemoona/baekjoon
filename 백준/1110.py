#1110
score=0
n=int(input())
num=n
while True:
    a=n//10
    b=n%10
    c=(a+b)%10
    n=b*10+c
    score+=1
    if num==n:
        break
print(score)