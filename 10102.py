# 개표

s=int(input())
p=input()
if len(p)==s: #입력한 인원수대로 나오게 하기 위해 
    a=p.count("A")
    b=p.count("B")
    if a==b:
        print("Tie")
    elif a>b:
        print("A")
    else:
        print("B")