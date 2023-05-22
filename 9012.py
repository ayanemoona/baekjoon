# 괄호
# 하나 씩 정답을 맞추는건 맞췄지만 여러개를 한번에 맞추는건 시간이 없어서 못함
# 너무 많은 시간을 쏟았다 학기 중에
s=int(input())
result=[]


for i in range(s):
    num=[]
    a=input()
    a1=list(a)

    if a1[0]==')':
        result.append('No')
        continue
    elif a1[0]=='(':
        num.append("(")
        for i in range(1,len(a1)):
            if a1[i]=="(":
                num.append('(')
            elif a1[i]==')':
                if len(num)==0:
                    result.append('No')
                    num.append('(')
                    break
                else:
                    num.remove('(')

        if "(" not in num:
            result.append('Yes')
            continue

                
print(result)
# 구글에서 퍼온거
# 얼추 아이디어는 비슷해서 뿌듯하다
n = int(input())

for i in range(n) :
    ps = input()
    ps_lst = list(ps)
    sum = 0
    for j in ps_lst :
        if j == "(" :
            sum += 1
        elif j == ")" :
            sum -= 1
        if sum < 0 :     	## 반복문 내에 있는 조건문 조건(2)를 만족하기 위해서.
            print("NO")
            break

    if sum > 0 :			## 조건(1)을 만족하기 위한 조건문.
        print("NO")
    elif sum == 0:
        print("YES")