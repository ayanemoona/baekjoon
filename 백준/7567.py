# 그릇
s=list(input())
A=s[0]
score=10
for i in range(1,len(s)):
    if A==s[i]:
        score+=5
        A=s[i]
    elif A!=s[i]:
        score+=10
        A=s[i]
print(score)
# 전과는 달리 반복수를 많이 줄였다