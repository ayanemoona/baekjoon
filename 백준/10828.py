# 스택
# 오랜만에 나 혼자 힘으로 푼 문제 
# 주어진 문제가 조건이 세세해서 잘 풀 수 있었던 것 같다
# 123을 +=으로 넣으면 [1,2,3]으로 각각으로 들어간다...
s=int(input())
answer=[]
result=[]
for i in range(s):
    s1=list(map(str,input().split()))
    if s1[0]=='push':
        result.append(s1[1])
    elif s1[0]=='pop':
        if len(result)==0:
            answer.append('-1')
        else:
            pop_num=result.pop()
            answer.append(pop_num)
    elif s1[0]=='size':
        size_num=len(result)
        answer.append(size_num)
    elif s1[0]=="empty":
        if len(result)==0:
            answer.append('1')
        else:
            answer.append('0')
    elif s1[0]=="top":
        if len(result)==0:
            answer.append('-1')
        else:
            answer.append(result[-1])

for i in answer:
    print(i)