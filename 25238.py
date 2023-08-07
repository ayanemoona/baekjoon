A,B=map(int,input().split())
B=B*0.01
danege=A-(A*B)
if danege>=100:
    print(0)
else:
    print(1)