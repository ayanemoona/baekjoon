# 직각삼각형
A=[]
B=[]
while True:
    a=list(map(int,input().split()))
    
    if  0 in a:
        break
    A.append(a)
for i in range(len(A)):
    b=A[i][0]**2
    c=A[i][1]**2
    d=A[i][2]**2
    if d>b:
        if d>c:
            continue
        elif d<c:
            box=d
            d=c
            c=box
    elif d<b:
        box=d
        d=b
        b=box
        if d>c:
            continue
        elif d<c:
            box=d
            d=c
            c=box
    if b+c==d:
        B.append('right')
    else:
        B.append('wrong')
for i in B:
    print(i)    
# 보기의 예시를 다 따라할 수 있다, 그리고 3가지 요소의 크기가 큰 경우를 골라서 정렬하는 것도 구현 함..
while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  # 세 수가 0이면 break
    max_num = max(nums)
    nums.remove(max_num)  # 빗변의 길이는 직각삼각형 세변의 길이중 가장 길다.
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
# 비교 안하고 맥스 써도 좋구나.. 
#