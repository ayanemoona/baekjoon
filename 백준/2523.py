N=int(input())
star='*'
num=1
for i in range(2*N-1):
    if i>=N-1:
        print(star*num)
        num-=1
    else:
        print(star*num)
        num+=1

