N=int(input())
A=[]
for i in range(N):
    x,y=map(int,input().split())
    A.append([x,y])
A.sort(key=lambda x:(x[0],x[1]))
for x,y in A:
    print(x,y)

# 2차원 숫자형 리스트 출력
# # 정렬할 때 기준을 만ㄷ르어서 함