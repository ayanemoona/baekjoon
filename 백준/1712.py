A,B,C=map(int,input().split())

if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)

#최대한 줄였는데도 연산 자체가 런타임 에러 만드네.ㅎ
#시간 연산>>비교