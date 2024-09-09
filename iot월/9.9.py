# a=input()
# a=ord(a)+1  # 문자-> 숫자
# print(chr(a)) # 숫자-> 문자

#1408
# a=input()
# for i in a:
#     i=ord(i)+2
#     print(chr(i),end='')
# print()

# for i in a:
#     i=(ord(i)*7)%80 +48
#     print(chr(i),end='')

#1295
# a=input()
# for i in a:
#     if i.islower(): # 소문자이면
#         print(i.upper(),end='')
#     elif i.isupper():
#         print(i.lower(),end='') #대문자이면
#     else:
#         print(i,end='')

# 2762
# a=input()
# for i in a:
#     if i.isupper():
#         print(i,end='')

# 1172
# a=list(map(int,input().split()))
# a.sort()
# print(*a)

#4501
# lst=[]
# for i in range(7):
#     a=int(input())
#     lst.append(a)
# lst.sort()
# print(lst[-1])
# print(lst[-2])

# #4531
# lst=[]
# for i in range(5):
#     a=int(input())
#     lst.append(a)
# lst.sort()
# print(sum(lst)//5)
# print(lst[2])

#6093
# a=int(input())
# lst=list(map(int,input().split()))
# print(*lst[::-1])

#4626
# a=int(input())
# lst=list(map(int,input().split()))
# sum=0
# jumsu=1

# for i in lst:
#     if i==1:
#         sum+=jumsu
#         jumsu+=1
#     else:
#         jumsu=1
# print(sum)

# #4591
# lst=[]
# for i in range(9):
#     a=int(input())
#     lst.append(a)

# print(max(lst))
# print(lst.index(max(lst))+1)

# #1352
# n=int(input())
# for i in range(n): # 세로 반복
#     for j in range(n): # 가로 반복
#         print('*',end='')
#     print() # 줄바꾸기

#1353
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

#1359
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

#1354
# a=int(input())
# for i in range(a,0,-1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

#1360
# a=int(input())
# for i in range(a,0,-1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

#1351
# a,b=map(int,input().split())
# for i in range(a,b+1):
#     for j in range(1,10):
#         print("%d*%d=%d"%(i,j,i*j))

#1380
# a=int(input())
# for i in range(1,7):
#     for j in range(1,7):
#         if i+j==a:
#             print(i,j)

#6080
# a,b=map(int,input().split())
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print(i,j)

#1362
# a=int(input())
# cnt=0
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         cnt+=1

# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(cnt,end=' ')
#         cnt-=1
#     print()

# #1361
# a=int(input())

# for i in range(a):
#     for j in range(i):
#         print(" ",end='')
#     print('**')

#1356
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if i==1 or i==a:
#             print('*',end='')
#         elif j==1 or j==a:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print()

#1355
# a=int(input())
# for i in range(a):
#     for j in range(i):
#         print(' ' ,end='')
#     print('*'*(a-i))

#1286
# lst=[]
# for i in range(5):
#     a=int(input())
#     lst.append(a)
# print(max(lst))
# print(min(lst))

#1405
# a=int(input())
# b=list(map(int,input().split()))
# for i in range(a):
#     print(*b)
#     c=b.pop(0)
#     b.append(c)

#1417
# a=list(map(int,input().split()))
# a.sort()
# print(a[-3])

# 4846
# a = int(input())
# sum = 0
# for i in range(a):
#     b, c = map(int,input().split())
#     sum+=c%b
# print(sum)

#4012
# #rank 알고리즘
# a=int(input())
# b=list(map(int, input().split()))
# rank = [1]*a
# for i in range(a):
#     for j in range(a):
#         if i==j:
#             continue
#         if b[i]<b[j]:
#             rank[i]+=1

# for i in range(a):
#     print(b[i],rank[i])

#1676
# a=int(input())
# lst=[]
# rank=[1]*a

# for i in range(a):
#     b=int(input())
#     lst.append(b)

# for i in range(a):
#     for j in range(a):
#         if i==j:
#             continue
#         if lst[i]<lst[j]:
#             rank[i]+=1
# for i in rank:
#     print(i)

#4041
# #문자로 받기
# a=input()
# print(int(a[::-1]))
# sum=0
# for i in a:
#     sum=sum+int(i)
# print(sum)

# #6095
# a=[[0] *19 for _ in range(19)] #2차원 0으로 구성
# b=int(input())
# for i in range(b):
#     x,y=map(int,input().split())
#     a[x-1][y-1]=1

# for i in range(19):
#     for j in range(19):
#         print(a[i][j],end=' ')
#     print()

#1500
# a,b=map(int,input().split())
# lst=[]
# for i in range(a):
#     c=list(map(int,input().split()))
#     lst.append(c)

# for i in range(a):
#     for j in range(b):
#         print(lst[i][j],end=' ')
#     print()

#1521
# sum=0
# a,b=map(int,input().split())
# lst=[]
# for i in range(a):
#     c=list(map(int,input().split()))
#     lst.append(c)

# for i in range(a):
#     for j in range(a):
#         if lst[i][j] == -1:
#             continue
#         if lst[i][j]+b>=0 and lst[i][j]+b<=5:
#             sum+=1
# print(sum)

#1508
# a=int(input())
# lst=[[0]*a for i in range(a)]

# for i in range(a):
#     b=int(input())
#     lst[i][0] =b

# for i in range(a):
#     for j in range(i+1):
#         if lst[i][j] == 0:
#             lst[i][j] =lst[i][j-1] - lst[i-1][j-1]

# for i in range(a):
#     for j in range(i+1):
#         print(lst[i][j], end=' ' )
#     print()

#1805
# lst = []
# a = int(input())
# for i in range(a):
#     b, c = map(int,input().split())
#     lst.append([b,c])
# lst.sort()
# for i in lst:
#     print(*i)

#1207
# y={1:"도",2:"개",3:"걸",4:"윷",0:"모"}
# a = list(map(int,input().split()))
# print(y[sum(a)])

#1720
# a=int(input())
# for i in range(a):
#     b,c,d,e = map(int,input().split())
#     tmp =[b,c,d]
#     if min(tmp) == e:
#         continue
#     else:
#         print(i+1, min(tmp))
#         exit(1)#완전히 종료
# print(-1)

# #2009
# a,b = map(int,input().split())
# coffee =0

# while True:
#     if a<b:
#         break
#     a = a - b
#     coffee += 1
#     a = a + 1
# print(coffee)

#2037
# a=int(input())
# lst=[]
# for i in range(a,1000):
#     if i//a ==1:
#         lst.append(i)
# print({*lst})

#2333
# a=input()
# b=input()
# if b in a:
#     print('O')
# else:
#     print('X')

#2411
# male=0
# female = 0
# a=int(input())
# for i in range(a):
#     b=input().split(',')
#     if b[1] == 'F':
#         female+=1
#     else:
#         male+=1
# print(male)
# print(female)

#2412
# sum = 0
# a = int(input())
# for i in range(a):
#     b=input().split(',')
#     sum+=int(b[2])
# print("%.2f"%(sum/a)) 

# #2413
# sum = 0
# a = int(input())
# for i in range(a):
#     b=input().split(',')
#     sum+=int(len(b[3:]))
# print("%.2f"%(sum/a)) 

# a = int(input())
# sum = 0
# for i in range(a):
#     b=input()
#     sum=sum + b.count(',') - 2
# print("%.2f"%(sum/a))

#2761
# a, b=map(int, input().split(' '))
# lst = [a+b, a-b, a*b]
# lst.sort()
# print(lst[1])