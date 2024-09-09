#설탕배달
s=int(input())
box=0
if s%5==0:
    box+=s//5
else:
    if s//5==0:
        box+=-1
    else:
        a=s%5
        box+=s//5
        if a%3==0:
            box+=a//3
        else:
            if a//3==0:
                box+=1
            else:
                b=a%3
                box+=a//3
                if b%3!=0:
                    box+=1
print(box)
# 보기로 주어진 경우의 수를 다 맞췄다
# 딱 떨어졌을 경우도 고려하였다..
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)