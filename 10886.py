#0 = not cute / 1 = cute 
#쉬운 문제중 하나 0과 1번이 같은 숫자로 나왔을때도 고려를 안했다.
s=int(input())
not1=0
yes=0
for i in range(s):
    a=int(input())
    if a==0:
        not1+=1
    else:
        yes+=1
if not1>yes:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
