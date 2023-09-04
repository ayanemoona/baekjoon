N=int(input())
nothing=2*N-2
star=1
for i in range(1,2*N):
    print('*'*star+' '*nothing+'*'*star)
    if i>=N:
        star-=1
        nothing+=2
    else:
        star+=1
        nothing-=2

