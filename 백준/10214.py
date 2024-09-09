Yonsei=0
Korea=0
s=int(input())
for i in range(s):
    for j in range(9):
        a,b=map(int,input().split())
        Yonsei+=a
        Korea+=b
    if Yonsei==Korea:
        print("Draw")
    elif Yonsei<Korea:
        print("Korea")
    else:
        print("Yonsei")
