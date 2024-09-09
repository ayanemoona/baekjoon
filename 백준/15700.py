N,M=map(int,input().split())
count=0
if N>=M:
    Max=N
    Min=M
else:
    Max=M
    Min=N
count+=(Max//2)*(Min//1)

if Max%2==1 and Min>=2:
    count+=Min//2
print(count)
# 그림 그려서 알아냈다