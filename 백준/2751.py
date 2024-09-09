#수 정렬하기 2
s=int(input())
num=[]
for i in range(s):
    s1=int(input())
    num.append(s1)
num.sort()
for i in num:
    print(i)
# 간단한 식이지만 시간초과가 떠서 알아보니 python3 가 아니라 pypy3에다가 제출해야 하는 것이였다.
