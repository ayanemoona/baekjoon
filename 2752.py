# 내림차순 정렬
# 숫자형 리스트 join

a=list(map(int,input().split()))
a.sort(reverse=False)
c=[str(d)for d in a]
print(" ".join(c))