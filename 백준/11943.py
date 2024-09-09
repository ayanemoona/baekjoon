A,B=map(int,input().split())
C,D=map(int,input().split())
move=0
if A+D>=B+C:
    move+=B+C
elif A+D<B+C:
    move+=A+D
print(move)

# 열심히 하나하나 비교해보는거 였는데 결국 합계였다
# 그래도 포기하지 않고 계속 해서 해결함