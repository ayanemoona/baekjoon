# 소수 찾기
s=int(input())
a=list(map(int,input().split()))
num=0
if len(a)==s:
    for i in a:
        for j in [2,3,5,7,11,13]:
            if i//j==1 and i%j==0:
                num+=1
                break
            else:
                continue
print(num)
# 단점 : 더 많은 소수가 있을 텐데 (예를 들어 23도 가능하고) 2,3,5,7,11,13의 소수 밖에 못 찾음
n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)