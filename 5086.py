answer=[]
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:  # 0 0 을 입력 받았을때 중단
        break
    if b%a==0: # 첫번째 숫자가 두번째 숫자의 약수
        answer.append("factor")
    elif a%b==0:
        answer.append("multiple")
    else:
        answer.append("neither")
for i in answer:
    print(i)