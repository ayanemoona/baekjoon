#전자레인지
s=int(input())
answer=[0,0,0]
answer[0]+=s//300
a=s%300
answer[1]+=a//60
b=a%60
answer[2]+=b//10

if b%10!=0:
    print(-1)
else:
    print(" ".join(map(str, answer)))
# 처음부터 넘 어렵게 생각해서 if문으로 타고타고 들어가는 걸로 했는데 넘 복잡해져서 바꾸었다.
#숫자형 리스트는 join으로 출력이 안되서 찾아보니 map을 사용하는 방법이 있었다