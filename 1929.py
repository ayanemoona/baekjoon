# 소수 구하기
a,b= map(int, input().split())
sosu = []
for num in range(a,b+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu .append(num)  # error가 없으면 소수.

for i in range(sosu):
    print(i)
# 앞선 문제 1978번을 이용해 소수문제를 해결하였지만 시간초과
# 주어진 문제부터 시간 초가 짧다 2초
def prime(num):
    if num <2:
        return False
    i=2
    while i*i<=num:
        if num %i==0:
            return False
        i+=1
    return True
m,n=map(int,input().split())

for i in range(m,n+1):
    if prime(i):
        print(i)
# 함수를 이용해서 시간을 줄일 수 있다니.. 나도 다음부터 함수를 이용해서 백준을 풀어야 겠다.   