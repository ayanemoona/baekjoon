# 약수들의 합
answer=[]
while True:
    A=[]
    sum=0
    s=int(input())
    if s==-1:
        break
    for i in range(1,s):
        if s%i==0:
            A.append(i)
            sum+=i
    if s!=sum:
        ans=str(s)+' is NOT perfect.'
        answer.append(ans)
    elif s==sum:
        C=' + '.join(str(e) for e in A)  # 숫자를 문자열로 바꾼담에 join 
        ans=str(s)+" = "+C
        answer.append(ans)
for i in answer:
    print(i)
        
# join은 문자열만 합치므로 숫자를 문자열로 바꿔야함